from django.contrib import admin

from .models import CustomUser, Pet

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Pet)
