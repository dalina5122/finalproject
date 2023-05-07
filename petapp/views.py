from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseBadRequest
import json
from .models import Cat, Dog, Comments_Dog, Comments_Cat
from users.models import CustomUser
from users.forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes, authentication_classes

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

# GET INDIVIDUAL DOG
@csrf_exempt
@api_view(['GET'])
def dogdetails(request, dog_id):
    print("dog_id:", dog_id)
    try:
        dog = Dog.objects.get(id=dog_id)
        print("Found dog:", dog)
        return JsonResponse({'dog': dog.to_dict()})

    except Dog.DoesNotExist:
        print("Dog not found")
        return JsonResponse({'error': 'Dog not found'}, status=404)

# LIST OF COMMENTS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments_d(request, dog_id):
    comments = Comments_Dog.objects.filter(dog=dog_id).order_by('-timestamp_d')
    comments_data = [
        {
            'user': {
                'id': comment.user.id,
                'username': comment.user.username
            },
            'dog': comment.dog.id,
            'content_d': comment.content_d,
            'timestamp_d': comment.timestamp_d.isoformat(),
        }
        for comment in comments
    ]
    return JsonResponse(comments_data, safe=False)

# POST NEW COMMENT
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment_d(request):
    user = request.user
    dog_id = request.data['dog']
    content = request.data['content_d']

    dog = Dog.objects.get(id=dog_id)

    comment = Comments_Dog(user=user, dog=dog, content_d=content)
    comment.save()

    response_data = {
        'user': {
            'id': comment.user.id,
            'username': comment.user.username
        },
        'dog': comment.dog.id,
        'content_d': comment.content_d,
        'timestamp_d': comment.timestamp_d.isoformat(),
    }

    return JsonResponse(response_data, safe=False)

# -----------------------------------------------------------------------------------------------------

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

# GET INDIVIDUAL CAT
@csrf_exempt
@api_view(['GET'])
def catdetails(request, cat_id):
    print("cat_id:", cat_id)
    try:
        cat = Cat.objects.get(id=cat_id)
        print("Found cat:", cat)
        return JsonResponse({'cat': cat.to_dict()})

    except Cat.DoesNotExist:
        print("Cat not found")
        return JsonResponse({'error': 'Cat not found'}, status=404)

# LIST OF COMMENTS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments_c(request, cat_id):
    comments = Comments_Cat.objects.filter(cat=cat_id).order_by('-timestamp_c')
    comments_data = [
        {
            'user': {
                'id': comment.user.id,
                'username': comment.user.username
            },
            'cat': comment.cat.id,
            'content_c': comment.content_c,
            'timestamp_c': comment.timestamp_c.isoformat(),
        }
        for comment in comments
    ]
    return JsonResponse(comments_data, safe=False)

# POST NEW COMMENT
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment_c(request):
    user = request.user
    cat_id = request.data['cat']
    content = request.data['content_c']

    cat = Cat.objects.get(id=cat_id)

    comment = Comments_Cat(user=user, cat=cat, content_c=content)
    comment.save()

    response_data = {
        'user': {
            'id': comment.user.id,
            'username': comment.user.username
        },
        'cat': comment.cat.id,
        'content_c': comment.content_c,
        'timestamp_c': comment.timestamp_c.isoformat(),
    }

    return JsonResponse(response_data, safe=False)