from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name='auction/home.html'), name='home'),
    # path('api/dogs', views.newdog_api),
]