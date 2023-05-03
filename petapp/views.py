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

from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import QueryDict

from django.utils.decorators import method_decorator

def index(request):
    return render(request, "frontend/index.html", {})

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

# DOGS COMMENT SECTION
class DogCommentsView(View):
    @method_decorator(csrf_exempt, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        print('GET request parameters:', request.GET)  # Debug print
        dog_id = request.GET.get('dog_id', None)
        print('GET request dog_id:', dog_id)  # Debug print

        if dog_id:
            try:
                dog = Dog.objects.get(id=dog_id)
                comments = Comments_Dog.objects.filter(dog=dog).select_related('user')

                comments_json = []

                for comment in comments:
                    comments_json.append({
                        'id': comment.id,
                        'user': {
                            'username': comment.user.username
                        },
                        'content_d': comment.content_d,
                        'timestamp_d': comment.timestamp_d
                    })

                return JsonResponse(comments_json, safe=False)

            except Dog.DoesNotExist:
                pass

        return JsonResponse({"error": "Invalid request: Missing or invalid dog_id"}, status=400)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        dog_id = body.get('dog_id', None)
        content_d = body.get('content_d', None)

        print('POST request body:', body)  # Debug print
        print('POST request dog_id:', dog_id)  # Debug print
        print('POST request content_d:', content_d)  # Debug print

        print('Request headers:', request.META)
        print('Request user:', request.user)

        if request.user.is_authenticated and dog_id and content_d:
            try:
                dog = Dog.objects.get(id=dog_id)

                new_comment = Comments_Dog.objects.create(
                    user=request.user,
                    dog=dog,
                    content_d=content_d
                )

                comment_json = {
                    'id': new_comment.id,
                    'user': {
                        'username': new_comment.user.username
                    },
                    'content_d': new_comment.content_d,
                    'timestamp_d': new_comment.timestamp_d
                }

                print('Comment JSON:', comment_json)  # Debug print
                return JsonResponse(comment_json, status=201)

            except Dog.DoesNotExist:
                print('Dog.DoesNotExist')  # Debug print
                pass

        else:
            print('Not authenticated, dog_id, or content_d missing')

        return JsonResponse({"error": "Invalid request"}, status=400)