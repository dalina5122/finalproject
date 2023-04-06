from django.db import models
from django.contrib.auth.models import AbstractUser

from users.models import User

# GENDER_CHOICES=(
#     ('female'),
#     ('male'),
#     ('unknown'),
# )

# class User(AbstractUser):
#     profile_image=models.ImageField(default='default.jpg', upload_to='profile_images/')
#     date_of_birth=models.DateField(null=True)

#     def __str__(self):
#         """
#         Display the object name when printing the object
#         """
#         return self.username

#     def to_dict(self):
#         """
#         Use this to return a dictionary of the User object
#         """
#         return{
#             'id': self.id,
#             'date_of_birth': self.date_of_birth,
#             'username' : self.username,
#             'email' : self.email,
#             'profile_image' : self.profile_image.url,
#         }

class Pet(models.Model):
    picture=models.ImageField(upload_to='pet_images', blank=True, null=True)
    age=models.IntegerField()
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    color=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
    date=models.DateField(null=True)
    breed=models.CharField(max_length=200)
    # gender=models.CharField(max_length=3, choices=GENDER_CHOICES, default='unknown')
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """
        Display the object name when printing the object
        """
        return self.name

    def to_dict(self):
        """
        Use this to return a dictionary of the Answer object
        """
        return{
            'id': self.id,
            'picture': self.picture.url,
            'age': self.age,
            'name': self.name,
            'location': self.location,
            'color': self.color,
            'description': self.description,
            'date': self.date,
            'breed': self.breed,
            # 'gender': self.gender,
            'user': self.user.id,
        }