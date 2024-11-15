from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  dark_mode = models.BooleanField(default=False)
  wallpaper = models.ImageField(blank=True, null=True)

  def __save__(self, *args, **kwargs):
     super().save(*args, **kwargs)

  def __str__(self):
     return f'{self.username}' if not self.email else f'{self.username} - {self.email}'

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", blank=False, null=False)
    contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contact", blank=False, null=False)
    blocked = models.BooleanField()
    nickname = models.CharField(default=user.name, max_length=200)

    def __str__(self):
       return self.contact.username
