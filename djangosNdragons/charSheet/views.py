from django.shortcuts import render, redirect
#from .models import Note, Tag
from .serializers import RaceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
import urllib
import requests


def index(request):
    return

@api_view(['GET'])
def api_race(request, name):
    r = requests.get(f'https://api.open5e.com/races/{name}')
    print(r)
    try:
        race = request.results.get(slug=name)
    except request.DoesNotExist:
        raise Http404()
    serialized_note = RaceSerializer(race)
    return Response(serialized_note.data)