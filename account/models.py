from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    age = models.IntegerField()
    gender_choices = (
      ('Male', 'Male'),
      ('Female','Female'),
      ('Other','Other'),
      ('I prefer not to tell','I prefer not to tell'),
    )
    gender = models.CharField(max_length=50, choices = gender_choices)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
      return f'{self.user}, {self.age}, {self.gender}, {self.avatar}'