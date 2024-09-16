from django.urls import path, include
from .views import LoginView, UserCreateView

urlpatterns = [
    path('v1/login', LoginView.as_view(), name='login'),
    path('v1/register', UserCreateView.as_view(), name='register'),
]

