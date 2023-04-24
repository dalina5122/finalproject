from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

from users.views import signup, get_signup

from django.contrib import admin


urlpatterns = [
    # path('', TemplateView.as_view(template_name='auction/home.html'), name='home'),
    # path('api/dogs', views.newdog_api),
    path('signup/', signup, name='signup'),
    path('getsignup/', get_signup, name='getsignup'),
    path("admin/", admin.site.urls),
]