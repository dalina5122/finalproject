from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseBadRequest
import json
from .models import Cat, Dog, Comments_Dog
from users.models import CustomUser
from users.forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

import base64
from django.core.files.base import ContentFile

from rest_framework.authtoken.models import Token

def index(request):
    return render(request, "petapp/index.html", {})

# LIST OF DOGS
@csrf_exempt
@api_view(['GET'])
def getdogs(request):
    print('Request META:', request.META)
    print('Token in header:', request.META.get('HTTP_AUTHORIZATION'))
    print('Authenticated user:', request.user)
    return JsonResponse({
        'dogs': [
            dog.to_dict()
            for dog in Dog.objects.all()
        ]
    })

# POSTING DOG
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newdog(request):
    print('Token in header:', request.META.get('HTTP_AUTHORIZATION'))

    if request.method=='POST':
        print("Received data:", request.body.decode('utf-8'))
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
            owner=owner
        )
        return JsonResponse({'dog': dog.to_dict()})

# LIST OF CATS
@csrf_exempt
@api_view(['GET'])
def getcats(request):
    print('Request META:', request.META)
    print('Token in header:', request.META.get('HTTP_AUTHORIZATION'))
    print('Authenticated user:', request.user)
    return JsonResponse({
        'cats': [
            cat.to_dict()
            for cat in Cat.objects.all()
        ]
    })

# POSTING CAT
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newcat(request):
    print('Token in header:', request.META.get('HTTP_AUTHORIZATION'))

    if request.method=='POST':
        print("Received data:", request.body.decode('utf-8'))
        print('in post')
        print(request.user)
        print(request.FILES)
        owner=request.user

        data = json.loads(request.body)
        print("Received data:", data)
        image_data = data.get("picture_c")
        image_content = None
        if image_data:
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            image_content = ContentFile(base64.b64decode(imgstr), name=f'{request.POST.get("name_c")}.{ext}')

        cat = Cat.objects.create(
            name_c=data.get('name_c'),
            age_c=data.get('age_c'),
            county_c=data.get('county_c'),
            color_c=data.get('color_c'),
            description_c=data.get('description_c'),
            date_c=data.get('date_c'),
            breed_c=data.get('breed_c'),
            gender_c=data.get('gender_c'),
            status_c=data.get('status_c'),
            picture_c=image_content,
            owner=owner
        )
        return JsonResponse({'cat': cat.to_dict()})