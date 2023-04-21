from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Cat, Dog

from users.models import CustomUser

from django.contrib.auth import get_user_model

CustomUser = get_user_model()

if admin.site.is_registered(CustomUser):
    admin.site.unregister(CustomUser)

admin.site.register(CustomUser)
admin.site.register(Cat)
admin.site.register(Dog)
