from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    username=models.CharField(max_length=225)
    email=models.EmailField(max_length=225)
    password=models.CharField(max_length=225)

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task=models.CharField(max_length=225)
    
    def __str__(self):
        return self.task