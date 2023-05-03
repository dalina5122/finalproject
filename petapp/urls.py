from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

from users.views import signup, login_user

from django.contrib import admin

from .views import DogCommentsView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path("admin/", admin.site.urls),
    path('newdog/', views.newdog, name='newdog'),
    path('getdogs/', views.getdogs, name='getdogs'),
    path('dogscomments/', DogCommentsView.as_view(), name='dogscomments'),
]