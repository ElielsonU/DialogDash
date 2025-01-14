from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, Message, Participant
from datetime import datetime
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        if not user.is_authenticated:
          return await self.close()

        self.id = self.scope['url_route']['kwargs']['id']
        self.chat = await database_sync_to_async(Chat.objects.get)(id=self.id)
        if (not self.id): return self.disconnect(1000)
        self.room_group_name = f'chat_{self.id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        origin = text_data_json.get('origin', False)
        if (origin):
          participant = await database_sync_to_async(Participant.objects.get)(chat=self.chat, user=self.scope['user'])
          await database_sync_to_async(Message.objects.create)(
              participant=participant,
              created_at=datetime.now(),
              chat=self.chat,
              text=message
          )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'senderId': self.scope['user'].id,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        senderId = event['senderId']

        await self.send(text_data=json.dumps({
            'message': message,
            "senderId": senderId
        }))
