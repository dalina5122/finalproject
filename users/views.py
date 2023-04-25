from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    #     form = SignUpForm()
    # return render(request, 'signup.html', {'form': form})

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

# def csrf_middleware(get_response):
#     def middleware(request):
#         response = get_response(request)
#         response["X-CSRFToken"] = request.COOKIES.get("csrftoken")
#         return response
#     return middleware
