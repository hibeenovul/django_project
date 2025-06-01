from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField



class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    country = CountryField(blank_label = '(select country)')
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    state_of_residence = models.CharField(max_length=100)
    linkedin_profiles = models.URLField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

# Create your models here.
