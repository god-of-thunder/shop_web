from django.urls import path,include,re_path
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

users = DefaultRouter()
users.register(r"",views.UsersViewSet)
routers = DefaultRouter()
routers.register(r"",views.ProductViewSet)

urlpatterns = [
    path('',views.main),
    path('index/',views.index),
    path('users/',include(users.urls)),
    re_path(r"^patch_email/$",views.patch_email,name="patch_email"),
    path('enable/<str:key1>', views.enable, name='enable'),
    path("items/<str:id>",views.items),
    path("search/<str:keyword>",views.search),
    path("cart/",views.cart),
    path("limited_item/",views.limited_item),
    path("limited_time_sale/",views.limited_time_sale),
    path("sellercenter/",views.sellercenter),
    path("product_ajax/",include(routers.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)