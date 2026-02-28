#define URL route for index() view
from django.urls import include, path
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu-items/', views.MenuItemViewSet.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemViewSet.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]