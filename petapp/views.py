from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseBadRequest
import json
from .models import Cat, Dog
from users.models import CustomUser
from users.forms import SignUpForm

from django_render import render_to_string


def newdog_api(request):
    if request.method == "GET":
        return JsonResponse({
            'dogs': [
                dog.to_dict()
                for dog in Dog.objects.all()
            ]
        })

    if request.method == "POST":
        owner = get_object_or_404(User, id = request.user.id)
        pet=Pet.objects.create(
            age_d=request.POST.get('age_d'),
            name_d=request.POST.get('name_d'),
            location_d=request.POST.get('location_d'),
            color_d=request.POST.get('color_d'),
            description_d=request.POST.get('description_d'),
            date_d=request.POST.get('date_d'),
            breed_d=request.POST.get('breed_d'),
            gender_D=request.POST.get('gender_d'),
            user=owner
        )
        return JsonResponse(dog.to_dict())

# SIGN UP
def signup(request):
    # return render(request, 'signup.html')
    html=render_to_string('signup.html')
    return JsonResponse('html', html)
