from django import forms
from .models import Dog
from users.models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class AddDog(forms.ModelForm):
    picture_d=forms.ImageField(widget=forms.FileInput)
    date_d=forms.DateField(widget=DateInput)

    class Meta:
        model=Dog
        fields= ['picture_d', 'age_d', 'name_d', 'county_d', 'color_d', 'description_d', 'date_d', 'breed_d', 'gender_d', 'status_d']

    def save(self, commit=True, owner=None):
        dog=super().save(commit=False)
        print(f'Owner ID before setting: {dog.owner_id}')
        if owner:
            dog.owner = owner
        print(f'Owner ID after setting: {dog.owner_id}')
        dog.save()
        return dog
