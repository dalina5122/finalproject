from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

from users.views import signup, login_user, login_form, get_user_details, update_image

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path("admin/", admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('loginform/', login_form, name='loginform'),
    path('newdog/', views.newdog, name='newdog'),
    path('getdogs/', views.getdogs, name='getdogs'),
    path('newcat/', views.newcat, name='newcat'),
    path('getcats/', views.getcats, name='getcats'),
    path('getuserdetails/', get_user_details, name='getuserdetails'),
    path('updateimage/', update_image, name='updateimage'),
    path('dogdetails/<int:dog_id>', views.dogdetails, name='dogdetails'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.PET_IMAGES_URL, document_root=settings.PET_IMAGES_ROOT)
    urlpatterns += static(settings.PROFILE_IMAGES_URL, document_root=settings.PROFILE_IMAGES_ROOT)
