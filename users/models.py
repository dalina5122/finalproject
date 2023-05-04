from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import os

class CustomUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    profile_image=models.ImageField(default='default.jpg', upload_to='profile_images/')
    date_of_birth=models.DateField(null=True)
    dogs=models.ManyToManyField(to='petapp.Dog', blank=True)

    def __str__(self):
        return self.username

    def to_dict(self):
        domain = 'http://127.0.0.1:8000'
        profile_image_url = domain+settings.PROFILE_IMAGES_URL+os.path.basename(str(self.profile_image))
        return{
            'id': self.id,
            'date_of_birth': self.date_of_birth,
            'username' : self.username,
            'email' : self.email,
            'profile_image' : profile_image_url,
        }
