from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Pet

from users.models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Pet)
