from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login

from rest_framework.decorators import permission_classes, authentication_classes, api_view, parser_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.decorators import login_required

from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser

# SIGN UP
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            return JsonResponse({'success': True, 'user_id': user.id})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# LOG IN
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

def login_form(request):
    return render(request, 'login.html')

# GET DETAILS OF LOGGED IN USER
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_user_details(request):
    token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    token = Token.objects.get(key=token_key)
    user = token.user
    user_details = user.to_dict()
    return JsonResponse({'user': user_details})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_user_id(request):
    token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    token = Token.objects.get(key=token_key)
    user = token.user
    return JsonResponse({'id': user.id})

# PROFILE IMAGE UPDATE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@parser_classes([MultiPartParser])
def update_image(request):
    image = request.FILES['image']
    user = request.user
    user.profile_image.delete(save=False)
    user.profile_image = image
    user.save()
    user_details = user.to_dict()
    return Response({'user': user_details})


