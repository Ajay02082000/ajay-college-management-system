from django.db import models
from datetime import datetime

# Create your models here.
class fcltdetails(models.Model):
    fcltName = models.CharField(max_length=250)
    fcltDepartment = models.CharField(max_length=250)
    fcltMailid = models.EmailField(max_length=150)
    fcltphone_no = models.IntegerField(default=0)
    fcltAddress = models.CharField(max_length=250)
    

def __str__(self):
    return self.fcltName

class fcltleave(models.Model):
    teachername = models.CharField(max_length=250)
    leavetype = models.CharField(max_length=250)
    leavestartdate = models.DateField()
    leaveenddate = models.DateField()

def __str__(self):
    return self.teachername 
