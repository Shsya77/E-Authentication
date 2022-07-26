from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import send_mail
import environ

from .models import CustomUser
from .forms import UserRegisterForm
from .utils import send_otp
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

def home(request):
    return render(request, 'users/home.html')


@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account was created successfully!')
            user = authenticate(username=username,
                                password=form.cleaned_data['password1'])
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/landingpage')
            else:
                pass
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')


def landingpage(request):
    return render(request, 'users/landingpage.html')


def otp(request):
   if request.user:
        user = CustomUser.objects.filter(username=request.user.username).first()
        otp_val = random.randrange(100000, 999999)
        user.otp = otp_val
        user.save()

        send_otp(user.otp, user.phone)
        return render(request, 'users/otp.html')

def otp_handler(request):
    if request.user and request.method=='POST':
        user = CustomUser.objects.filter(username=request.user.username).first()
        otp_value = request.POST['otp']
        if user.otp == otp_value:
            user.is_verified = True
            user.save()
            messages.success(request, "Account verified")
            return redirect('/profile')
        messages.error(request, "Otp is invalid")
        return redirect('/')



def qr_code(request):
     if request.user:
        user = CustomUser.objects.filter(username=request.user.username)
        otp_val = random.randrange(100000, 999999)
        user.otp = otp_val
        return render(request,'users/qr_code.html')    