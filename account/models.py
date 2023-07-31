from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  avatar = models.ImageField(null=True, blank=True, upload_to="avatar")
  def __str__(self):
    return f"{self.user} - {self.avatar}"