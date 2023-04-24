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
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'date_of_birth': form.cleaned_data['date_of_birth'],
                'profile_image': str(form.cleaned_data['profile_image']),
                'password1': form.cleaned_data['password1'],
                'password2': form.cleaned_data['password2'],
            }
            return JsonResponse(form_data)
    return JsonResponse({'error': 'Invalid form data.'})