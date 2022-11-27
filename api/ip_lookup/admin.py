from django.contrib import admin
from .models import IPv4Model, IPv6Model
# Register your models here.

admin.site.register(IPv4Model)
admin.site.register(IPv6Model)