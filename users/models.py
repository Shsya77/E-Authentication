from django.db import models
from phone_field import PhoneField


class Client(models.Model):
    
    phone_number = PhoneField(blank=True, help_text='Contact phone number')