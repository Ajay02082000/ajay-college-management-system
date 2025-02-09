from django.db import models

# Create your models here.
class prntdetails(models.Model):
    prntName = models.CharField(max_length=250)
    prntMailid = models.EmailField(max_length=150)
    prntphone_no = models.IntegerField(default=0)
    Feepaid = models.IntegerField(default=0)
    Feedue = models.IntegerField(default=0)

def __str__(self):
    return self.prntName

class fee(models.Model):
    studentname = models.CharField(max_length=250)
    studentid = models.CharField(max_length=250)
    feeamount = models.CharField(max_length=250)

def __str__(self):
    return self.studentname    

    