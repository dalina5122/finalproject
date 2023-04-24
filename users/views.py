from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def csrf_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response["X-CSRFToken"] = request.COOKIES.get("csrftoken")
        return response
    return middleware
