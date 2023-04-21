from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(UserCreationForm):
    profile_image=forms.ImageField(widget=forms.FileInput)
    date_of_birth=forms.DateField(widget=DateInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'profile_image', 'password1', 'password2']