from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('api/char', views.CharactersViewSet, basename='CharSheet')

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
    # path('api/char/<int:char_id>/', views.api_byId)
]
