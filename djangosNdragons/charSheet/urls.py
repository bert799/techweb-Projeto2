from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/races/<str:name>/', views.api_race),
]
