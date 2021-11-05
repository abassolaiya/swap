from django.urls import path, include

from rest_framework import routers

from .views import UserCreate, LoginView, UserViewSet, BusinessViewset

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('business', BusinessViewset, 'business')

urlpatterns = [
    path('user/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(),name='login'),
]
