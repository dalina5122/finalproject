from django.conf import settings

from django.db import models

from django.contrib.auth import get_user_model
CustomUser = get_user_model()

from django.utils import timezone

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
        ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomita'), ('IS', 'Iasi'), ('MM', 'Maramures'), ('MH', 'Mehedinti'), ('MS', 'Mures'),
        ('OT', 'Olt'), ('PH', 'Prahova'), ('SM', 'Satu Mare'), ('SJ', 'Salaj'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('TR', 'Teleorman'),
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
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    id=models.AutoField(primary_key=True, default=1)

    def __str__(self):
        """
        Display the object name when printing the object
        """
        return self.name_d

    def to_dict(self):
        """
        Use this to return a dictionary of the Answer object
        """
        return{
            'id': self.id,
            'picture_d': self.picture_d.url,
            'age_d': self.age_d,
            'name_d': self.name_d,
            'county_d': self.county_d,
            'color_d': self.color_d,
            'description_d': self.description_d,
            'date_d': self.date_d,
            'breed_d': self.breed_d,
            'gender_d': self.gender_d,
            'status_d': self.status_d,
            'username': self.username.id,
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
        ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomita'), ('IS', 'Iasi'), ('MM', 'Maramures'), ('MH', 'Mehedinti'), ('MS', 'Mures'),
        ('OT', 'Olt'), ('PH', 'Prahova'), ('SM', 'Satu Mare'), ('SJ', 'Salaj'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('TR', 'Teleorman'),
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
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    id=models.AutoField(primary_key=True, default=1)


    def __str__(self):
        """
        Display the object name when printing the object
        """
        return self.name_c

    def to_dict(self):
        """
        Use this to return a dictionary of the Answer object
        """
        return{
            'id': self.id,
            'picture_c': self.picture_c.url,
            'age_c': self.age_c,
            'name_c': self.name_c,
            'county_c': self.county_c,
            'color_c': self.color_c,
            'description_c': self.description_c,
            'date_c': self.date_c,
            'breed_c': self.breed_c,
            'gender_c': self.gender_c,
            'status_c':self.status_c,
            'username': self.username.id,
        }
