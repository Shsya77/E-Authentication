
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()
    
    class Meta:
        model = CustomUser
        fields = ['username','email', 'phone','password1','password2']