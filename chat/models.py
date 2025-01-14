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
  description = models.TextField(null=True, blank=False)
  max_size = models.IntegerField()
  image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default.png')

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
  
  def __str__(self):
    return self.subject
  
class Participant(models.Model):
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=False, null=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

  def __str__(self):
    return self.user.username

class Message(models.Model):
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=False, null=False)
  participant = models.ForeignKey(Participant, on_delete=models.CASCADE, blank=False, null=False)
  text = models.TextField(blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

  def __str__(self):
    return self.text