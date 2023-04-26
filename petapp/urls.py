from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

from users.views import signup, login

from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path("admin/", admin.site.urls),
]