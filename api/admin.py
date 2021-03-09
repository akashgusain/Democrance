from django.contrib import admin

from .models import Customer, Insurance

admin.site.register(Customer)
admin.site.register(Insurance)
