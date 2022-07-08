from django.db import models
from django.contrib.auth.models import AbstractUser #new

# Create your models here.
class CustomUser(AbstractUser): #new
    ACCOUNT_TYPE = [('1', 'Student'), ('2', 'Teacher')]
    accountType = models.CharField(max_length=1, choices=ACCOUNT_TYPE, default='1')
    classCode = models.CharField(max_length=30, blank=True)
    # Any extra fields would go here
    def __str__(self):
        return self.email

class Practice(models.Model):
  TYPE = [('1', 'Lesson'), ('2', 'Quiz')]
  email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  algorithm = models.CharField(max_length=30)
  type = models.CharField(max_length=1, choices=TYPE)
  score = models.IntegerField(null=True)

class Assignment(models.Model):
  email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  assignment = models.CharField(max_length=30)
  question = models.IntegerField()
  score = models.IntegerField(null=True)
  weight = models.IntegerField()
