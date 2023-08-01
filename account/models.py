from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.IntegerField()
    avatar = models.ImageField(null=True, blank=True, upload_to='avatar/')
    gender_choices = (
      ('Male', 'Male'),
      ('Female','Female'),
      ('Other','Other'),
      ('I prefer not to tell','I prefer not to tell'),
    )
    gender = models.CharField(max_length=50, choices = gender_choices, default='Other')

    def __str__(self):
        return str(self.user)