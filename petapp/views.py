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
    if request.method=='POST':
        form = AddDog(request.POST, request.FILES)
        if form.is_valid():
            dog=form.save(commit=False)
            dog.owner=request.user.username
            dog.save()
            return redirect('newdog')

    else:
        form=AddDog()
    return render(request, 'adddog.html', {'form': form})




