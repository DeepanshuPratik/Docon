from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("about",views.about, name='about'),
   path("services",views.services, name='services'),
   path("contact",views.contact, name='contact'),
   path("services/book",views.book, name='book'),
   path("services/report",views.report, name='report'),
   path("services/diag",views.diag, name='diag'),
]