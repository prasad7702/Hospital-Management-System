

# Create your models here.

from django.db import models

class PatientDetails(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=50)
    Mobile = models.BigIntegerField()
    Address = models.CharField(max_length=500)
    Problem = models.CharField(max_length=50)
    DoctorName = models.CharField(max_length=50)



