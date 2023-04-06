from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Pet

from users.models import User


admin.site.register(User)
admin.site.register(Pet)
