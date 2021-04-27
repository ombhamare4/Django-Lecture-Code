from django.db import models

# Create your models here.
#Here Create Database...

class Student(models.Model):
    name = models.CharField(max_length=20,default="No Name") #attribute are created
    roll = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.name)
     