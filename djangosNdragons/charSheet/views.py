from django.db.models.query_utils import subclasses
from django.shortcuts import render, redirect
#from .models import Note, Tag
from .serializers import CharSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Character
import urllib
import requests


def index(request):
    return

@api_view(['GET', 'POST'])
def api_character(request):
    try:
        print(Character.objects.all())
        char = Character.objects.all()
    except request.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        char = Character()
        new_char = request.data
        char.name = new_char['name']
        char.race = new_char['race']
        char.save()
    
    serialized_sheet = CharSerializer(char, many=True)
    return Response(serialized_sheet.data)