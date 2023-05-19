from django.db import models

# Create your models here.

class SexOptions(models.TextChoices):
    FEMALE = 'Female', 'Female'
    MALE = 'Male', 'Male'
    UNSURE = 'Unsure', 'Unsure'

class CStatusOptions(models.TextChoices):
    SINGLE      =   'Single', 'Single'
    MARRIED     =   'Married', 'Married'
    DIVORCED    =   'Divorced', 'Divorced'
    SEPARATED   =   'Separated', 'Separated'
    WIDOWED     =   'Widowed', 'Widowed'

class SitioOptions(models.TextChoices):
    ILAYA       =   'Ilaya', 'Ilaya'
    GHEIGHTS    =   'Green Heights', 'Green Heights'
    WHOUSE      =   'White House', 'White House'
    DELPIDIO    =   'Don Elpidio', 'Don Elpidio'
    SAMBAT      =   'Sambat', 'Sambat'
    PINAGPALA   =   'Pinagpala', 'Pinagpala'
    CENTRO      =   'Centro', 'Centro'

class Resident(models.Model):
    resID       =   models.IntegerField(primary_key=True, unique=True)
    firstName   =   models.CharField(max_length=50)
    lastName    =   models.CharField(max_length=50)
    middleName  =   models.CharField(max_length=50)
    birthday    =   models.DateField(auto_now=False, null=True, blank=True)
    sex         =   models.CharField(max_length=20, choices=SexOptions.choices)
    civilStatus =   models.CharField(max_length=20, choices=CStatusOptions.choices)
    sitio       =   models.CharField(max_length=20, choices=SitioOptions.choices)
    
    def __str__(self):
        return self.lastName
