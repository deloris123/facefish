from django.db import models


# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30)
    passcode = models.CharField(max_length=30)

    def __str__(self):
         return "name:" + str(self.username)