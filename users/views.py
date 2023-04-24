from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def get_signup(request):
    form = SignUpForm()
    form_data = {
        'username': form['username'],
        'email': form['email'],
        'date_of_birth': form['date_of_birth'],
        'profile_image': form['profile_image'],
        'password1': form['password1'],
        'password2': form['password2'],
    }
    return JsonResponse(form_data)