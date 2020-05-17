from django.db import models

# Create your models here.

class std(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname=models.CharField(max_length=100)
    RollNo = models.CharField(max_length=4)
    mobile = models.CharField(max_length=15)
    Std = models.ForeignKey(std,on_delete=models.CASCADE)#if we deleted std automatically deleted all the records
