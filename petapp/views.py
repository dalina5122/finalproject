from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseBadRequest
import json
from .models import Cat, Dog
from users.models import CustomUser
from users.forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import base64
from django.core.files.base import ContentFile

def index(request):
    return render(request, "frontend/index.html", {})

@login_required
@csrf_exempt
def newdog(request):
    if request.method=='GET':
        return JsonResponse({
            'dogs': [
                dog.to_dict()
                for dog in Dog.objects.all()
            ]
        })

    if request.method=='POST':
        print('in post')
        print(request.user)
        print(request.FILES)
        owner=request.user

        data = json.loads(request.body)
        print("Received data:", data)
        image_data = data.get("picture_d")
        image_content = None
        if image_data:
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            image_content = ContentFile(base64.b64decode(imgstr), name=f'{request.POST.get("name_d")}.{ext}')

        dog = Dog.objects.create(
            name_d=data.get('name_d'),
            age_d=data.get('age_d'),
            county_d=data.get('county_d'),
            color_d=data.get('color_d'),
            description_d=data.get('description_d'),
            date_d=data.get('date_d'),
            breed_d=data.get('breed_d'),
            gender_d=data.get('gender_d'),
            status_d=data.get('status_d'),
            picture_d=image_content,
            owner=user
        )
        return JsonResponse(dog.to_dict())






