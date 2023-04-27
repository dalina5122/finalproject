from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseBadRequest
import json
from .models import Cat, Dog
from users.models import CustomUser
from users.forms import SignUpForm
from .forms import AddDog

def index(request):
    return render(request, "frontend/index.html", {})

def newdog(request):
    if request.method=='POST':
        form = AddDog(request.POST, request.FILES)
        if form.is_valid():
            dog=form.save(commit=False)
            dog.username=request.user
            dog.save()
    else:
        form=AddDog()
    return render(request, 'adddog.html', {'form': form})




