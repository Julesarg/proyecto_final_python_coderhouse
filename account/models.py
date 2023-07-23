from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=40, default="")

    gender_choices = (
      ('Male', 'Male'),
      ('Female','Female'),
      ('Other','Other'),
      ('I prefer not to tell','I prefer not to tell'),
    )
    gender = models.CharField(max_length=50, choices = gender_choices)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f'Name: {self.name}, Lastname: {self.last_name}, Username: {self.username}, Email: {self.email}, Age: {self.age},  Password: {self.password}, Gender: {self.gender}, Profile Pic: {self.avatar}'