from django.urls import path
from .import views

urlpatterns = [
    path('', views.flames_home, name='flames_home'),
    path('result', views.result, name='result')
]