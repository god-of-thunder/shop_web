from django.urls import path,include,re_path
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

users = DefaultRouter()

urlpatterns = [
    path('',views.main),
    path('index/',views.index),
    path('users/',include(users.urls)),
    re_path(r"^patch_email/$",views.patch_email,name="patch_email"),
    path('enable/<str:key1>', views.enable, name='enable'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)