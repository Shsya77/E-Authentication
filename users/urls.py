from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('landingpage/',views.landingpage,name='landingpage'),
     path('otp/',views.otp,name='otp'),
     path('otp_handler', views.otp_handler, name='otp_handler'),
     path('qr_code/',views.qr_code,name='qr_code'),
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout')

]
