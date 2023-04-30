from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseBadRequest
import json
from .models import Cat, Dog
from users.models import CustomUser
from users.forms import SignUpForm
from .forms import AddDog
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "frontend/index.html", {})

@login_required
@csrf_exempt
def newdog(request):
    if request.method=='GET':
        return JsonResponse({
            'dogs': [
                dog.to_dict()
                for dog in Dogs.objects.all()
            ]
        })

    if request.methid=='POST':
        print('in post')
        print(request.user)
        print(request.FILES)
        user=get_object_or_404(CustomUser, id=request.owner.id)

        dog=Dogs.objects.create(
            name_d=request.POST.get('name_d'),
            age_d=request.POST.get('age_d'),
            county_d=request.POST.get('county_d'),
            color_d=request.POST.get('color_d'),
            description_d=request.POST.get('description_d'),
            date_d=request.POST.get('date_d'),
            breed_d=request.POST.get('breed_d'),
            gender_d=request.POST.get('gender_d'),
            status_d=request.POST.get('status_d'),
            picture_d=request.FILES.get('picture_d'),
            owner=user
        )
        return JsonResponse(dog.to_dict())

    # user_id = request.user.id
    # user = CustomUser.objects.get(id=user_id)

    # if request.method=='POST':
    #     form=AddDog(request.POST, request.FILES)
    #     if form.is_valid():
    #         dog=form.save(commit=False, owner=user)
    #         dog.save()
    #         return redirect('newdog')
    #     else:
    #         print(form.errors)

    # else: 
    #     form=AddDog()
    #     return render(request, 'adddog.html', {'form': form})



    # if request.method=='POST':
    #     form = AddDog(request.POST, request.FILES)
    #     if form.is_valid():
    #         dog=form.save(commit=False)
    #         dog.owner=request.user
    #         dog.save()
    #         return redirect('newdog')

    # else:
    #     form=AddDog()
    # return render(request, 'adddog.html', {'form': form})




