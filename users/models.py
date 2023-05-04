from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    profile_image=models.ImageField(default='default.jpg', upload_to='profile_images/')
    date_of_birth=models.DateField(null=True)
    dogs=models.ManyToManyField(to='petapp.Dog', blank=True)

    def __str__(self):
        """
        Display the object name when printing the object
        """
        return self.username

    def to_dict(self):
        """
        Use this to return a dictionary of the User object
        """
        return{
            'id': self.id,
            'date_of_birth': self.date_of_birth,
            'username' : self.username,
            'email' : self.email,
            'profile_image' : self.profile_image.url,
        }
