from django.db import models
from user.models import User

# Create your models here.
class Chat(models.Model):
  CHAT_TYPES_CHOICE = (
    ('GRP', 'Grupo'),
    ('CVS', 'Conversa'),
  )
  CHAT_SIZES_CHIOCES = {
    'GRP': 64,
    'CVS': 2,
  }
  type = models.CharField(max_length=3, choices=CHAT_TYPES_CHOICE, blank=False, null=False)
  subject = models.CharField(max_length=50, blank=False, null=False)
  description = models.TextField()
  max_size = models.IntegerField()

  def save(self, *args, **kwargs):
    self.max_size = self.CHAT_SIZES_CHIOCES.get(self.type)
    super().save(*args, **kwargs)
  
class Participant(models.Model):
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=False, null=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)