
from django.db import models


class Person(models.Model):
   
    username = models.CharField(max_length=100, verbose_name="Entered Email/Username")
    passcode = models.CharField(max_length=100, verbose_name="Entered Password")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Time Submitted")


    

    def __str__(self):
        return f"{self.username} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"





# from django.db import models


# # Create your models here.
# class Person(models.Model):
#     username = models.CharField(max_length=30)
#     passcode = models.CharField(max_length=30)

#     def __str__(self):
#          return "name:" + str(self.username)