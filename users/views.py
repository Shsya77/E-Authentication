from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import CustomUser
import random


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
            if not user:
                if user.is_active:
                    auth_login(request, user)
                return redirect('home')
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
        user = CustomUser.objects.filter(username=request.user.username)
        otp = random.randrange(100000, 999999)
        user.otp = otp
        return render(request, 'users/otp.html', {'otp':otp})

def qr_code(request):
    return render(request,'users/qr_code.html')    