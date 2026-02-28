#update URLConf by including URL patterns of restaurant app
from django import views
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from restaurant import views

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('restaurant.urls')),
   path('restaurant/booking/', include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken')),
]
   