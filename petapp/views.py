from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
import json

from .models import Index, DogsMap, CatsMap

from users.models import User


def newdog_api(request):
    if request.method == "GET":
        return JsonResponse({
            'pets': [
                pet.to_dict()
                for pet in Pet.objects.all()
            ]
        })

    if request.method == "POST":
        owner = get_object_or_404(User, id = request.user.id)
        pet=Pet.objects.create(
            age=request.POST.get('age'),
            name=request.POST.get('name'),
            location=request.POST.get('location'),
            color=request.POST.get('color'),
            description=request.POST.get('description'),
            date=request.POST.get('date'),
            breed=request.POST.get('breed'),
            user=owner
        )
        return JsonResponse(pet.to_dict())
