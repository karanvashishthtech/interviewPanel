from email.utils import format_datetime
from operator import mod
from django import forms
from django.db import models
#from sqlalchemy import true
from django.core.validators import RegexValidator
from interview import settings

# Create your models here.
class Employee(models.Model):

    live_status = (
        ('Complete','Complete'),
        ('In progress','In progress'),
        ('Pending','Pending')
    )
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    #phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=live_status,default='Pending')
    time = models.CharField(max_length=100)#TimeField(auto_now=False, auto_now_add=False)
    MobileNumber = models.CharField(max_length=100)#CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    Date = models.CharField(max_length=100)#DateField()

    def __str__(self):
        temp = '{0.name},{0.status},{0.time},{0.MobileNumber}'
        return temp.format(self)