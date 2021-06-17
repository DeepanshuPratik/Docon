from django.contrib import admin

from .models import UserDetails
from .models import Contact
from .models import Book
from .models import Diagnostic
from .models import Report

# Register your models here.

admin.site.register(UserDetails)
admin.site.register(Contact)
admin.site.register(Book)
admin.site.register(Diagnostic)
admin.site.register(Report)