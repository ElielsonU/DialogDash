import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.accept()
  def disconnect(self, code):
    pass
  def receive(self, text_data=None, bytes_data=None):
    return super().receive(text_data, bytes_data)