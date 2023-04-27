from django import forms
from .models import Dog

class DateInput(forms.DateInput):
    input_type = 'date'

class AddDog(forms.ModelForm):
    picture_d=forms.ImageField(widget=forms.FileInput)
    date_d=forms.DateField(widget=DateInput)

    class Meta:
        model=Dog
        fields= ['picture_d', 'age_d', 'name_d', 'county_d', 'color_d', 'description_d', 'date_d', 'breed_d', 'gender_d', 'status_d']
