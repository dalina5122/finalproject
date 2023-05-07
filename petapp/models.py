from django.conf import settings

from django.db import models

# from django.contrib.auth import get_user_model
# CustomUser = get_user_model()
CustomUser=settings.AUTH_USER_MODEL

from django.utils import timezone

import base64, os


class Dog(models.Model):
    GENDER_CHOICES_D = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    COUNTIES_D=[
        ('AB', 'Alba'), ('AR', 'Arad'), ('AG', 'Arges'), ('BC', 'Bacau'), ('BH', 'Bihor'), ('BN', 'Bistrita-Nasaud'), ('BT', 'Botosani'),
        ('BV', 'Brasov'), ('BR', 'Braila'), ('BZ', 'Buzau'), ('CS', 'Caras-Severin'), ('CL', 'Calarasi'), ('CJ', 'Cluj'),
        ('CT', 'Constanta'), ('CV', 'Covasna'), ('DB', 'Dambovita'), ('DJ', 'Dolj'), ('GL', 'Galati'), ('GR', 'Giurgiu'), ('GJ', 'Gorj'),
        ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomita'), ('IS', 'Iasi'), ('IF', 'Ilfov'), ('MM', 'Maramures'), ('MH', 'Mehedinti'), ('MS', 'Mures'),
        ('NT', 'Neamt'), ('OT', 'Olt'), ('PH', 'Prahova'), ('SM', 'Satu Mare'), ('SJ', 'Salaj'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('TR', 'Teleorman'),
        ('TM', 'Timis'), ('TL', 'Tulcea'), ('VS', 'Vaslui'), ('VL', 'Valcea'), ('VN', 'Vrancea'),
    ]

    STATUS_D=[
        ('L', 'Lost'),
        ('F', 'Found'),
        ('A', 'Adoption'),
    ]

    picture_d=models.ImageField(upload_to='pet_images', blank=True, null=True)
    age_d=models.IntegerField(default=0)
    name_d=models.CharField(max_length=200, default=' ')
    county_d=models.CharField(max_length=17, choices=COUNTIES_D, default=' ')
    color_d=models.CharField(max_length=50, default=' ')
    description_d=models.TextField(max_length=1000, default=' ')
    date_d=models.DateTimeField(default=timezone.now)
    breed_d=models.CharField(max_length=200, default=' ')
    gender_d=models.CharField(max_length=1, choices=GENDER_CHOICES_D, default=' ')
    status_d=models.CharField(max_length=8, choices=STATUS_D, default=' ')
    owner=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dogs_owned', null=True)

    def __str__(self):
        return self.name_d

    def to_dict(self):
        owner_id = self.owner.id if self.owner else None

        picture_base64 = ""
        if self.picture_d:
            image_path = os.path.join(settings.PET_IMAGES_ROOT, os.path.basename(self.picture_d.name))
            with open(image_path, "rb") as img_file:
                picture_base64 = base64.b64encode(img_file.read()).decode("utf-8")

        return{
            'id': self.id,
            'picture_d': picture_base64,
            'age_d': self.age_d,
            'name_d': self.name_d,
            'county_d': self.county_d,
            'color_d': self.color_d,
            'description_d': self.description_d,
            'date_d': self.date_d,
            'breed_d': self.breed_d,
            'gender_d': self.gender_d,
            'status_d': self.status_d,
            'owner': self.owner.id,
        }

class Cat(models.Model):
    GENDER_CHOICES_C = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    COUNTIES_C=[
        ('AB', 'Alba'), ('AR', 'Arad'), ('AG', 'Arges'), ('BC', 'Bacau'), ('BH', 'Bihor'), ('BN', 'Bistrita-Nasaud'), ('BT', 'Botosani'),
        ('BV', 'Brasov'), ('BR', 'Braila'), ('BZ', 'Buzau'), ('CS', 'Caras-Severin'), ('CL', 'Calarasi'), ('CJ', 'Cluj'),
        ('CT', 'Constanta'), ('CV', 'Covasna'), ('DB', 'Dambovita'), ('DJ', 'Dolj'), ('GL', 'Galati'), ('GR', 'Giurgiu'), ('GJ', 'Gorj'),
        ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomita'), ('IS', 'Iasi'), ('IF', 'Ilfov'), ('MM', 'Maramures'), ('MH', 'Mehedinti'), ('MS', 'Mures'),
        ('NT', 'Neamt'), ('OT', 'Olt'), ('PH', 'Prahova'), ('SM', 'Satu Mare'), ('SJ', 'Salaj'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('TR', 'Teleorman'),
        ('TM', 'Timis'), ('TL', 'Tulcea'), ('VS', 'Vaslui'), ('VL', 'Valcea'), ('VN', 'Vrancea'),
    ]

    STATUS_C=[
        ('L', 'Lost'),
        ('F', 'Found'),
        ('A', 'Adoption'),
    ]

    picture_c=models.ImageField(upload_to='pet_images', blank=True, null=True)
    age_c=models.IntegerField(default=0)
    name_c=models.CharField(max_length=200, default=' ')
    county_c=models.CharField(max_length=17, choices=COUNTIES_C, default=' ')
    color_c=models.CharField(max_length=50, default=' ')
    description_c=models.TextField(max_length=1000, default=' ')
    date_c=models.DateTimeField(default=timezone.now)
    breed_c=models.CharField(max_length=200, default=' ')
    gender_c=models.CharField(max_length=1, choices=GENDER_CHOICES_C, default=' ')
    status_c=models.CharField(max_length=8, choices=STATUS_C, default=' ')
    owner=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_c

    def to_dict(self):
        owner_id = self.owner.id if self.owner else None

        picture_base64 = ""
        if self.picture_c:
            image_path = os.path.join(settings.PET_IMAGES_ROOT, os.path.basename(self.picture_c.name))
            with open(image_path, "rb") as img_file:
                picture_base64 = base64.b64encode(img_file.read()).decode("utf-8")

        return{
            'id': self.id,
            'picture_c': picture_base64,
            'age_c': self.age_c,
            'name_c': self.name_c,
            'county_c': self.county_c,
            'color_c': self.color_c,
            'description_c': self.description_c,
            'date_c': self.date_c,
            'breed_c': self.breed_c,
            'gender_c': self.gender_c,
            'status_c':self.status_c,
            'owner': self.owner.id,
        }

class Comments_Dog(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    dog=models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
    content_d=models.TextField()
    timestamp_d=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content_d

class Comments_Cat(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    cat=models.ForeignKey(Cat, on_delete=models.CASCADE, null=True)
    content_c=models.TextField()
    timestamp_c=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content_c

