from django.contrib import admin
from django.urls import path, include
from home.views import homePage,signUpPage



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage),
    path('sign-up',signUpPage),
    path('',include('home.urls')),
    
]
