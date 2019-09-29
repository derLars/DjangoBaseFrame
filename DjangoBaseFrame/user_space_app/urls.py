from django.urls import path
from . import views

urlpatterns = [
    path('', views.userSpace, name='user_space'),
]