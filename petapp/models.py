from django.conf import settings

from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# from users.models import CustomUser

from django.utils import timezone

class Pet(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    picture=models.ImageField(upload_to='pet_images', blank=True, null=True)
    age=models.IntegerField(default=0)
    name=models.CharField(max_length=200, default=' ')
    location=models.CharField(max_length=200, default=' ')
    color=models.CharField(max_length=50, default=' ')
    description=models.TextField(max_length=1000, default=' ')
    date=models.DateTimeField(default=timezone.now)
    breed=models.CharField(max_length=200, default=' ')
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES, default=' ')
    # username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    pet_ptr = models.OneToOneField('self', on_delete=models.CASCADE, parent_link=True, primary_key=True, default=None)


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
            'gender': self.gender,
            'username': self.username.id,
        }

    # class Meta:
    #     abstract = True

class Dog(Pet):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Cat(Pet):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

