from django.db.models.query_utils import subclasses
from django.shortcuts import render, redirect
from .serializers import CharSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import Http404
from .models import Character
import urllib
import requests

class CharactersViewSet(viewsets.ModelViewSet):

    queryset = Character.objects.all()
    serializer_class = CharSerializer

# def index(request):
#     return

# @api_view(['GET', 'POST'])
# def api_characters(request):
#     try:
#         characters = Character.objects.all()
#     except request.DoesNotExist:
#         raise Http404()

#     if request.method == 'POST':
#         print(request.data)
#         char = Character()
#         new_char = request.data
#         char.name = new_char['nome']
#         char.race = new_char['raca']
#         char.playerClass = new_char['classe']
#         char.save()
    
#     serialized_sheet = CharSerializer(characters, many=True)
#     return Response(serialized_sheet.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def api_byId(request, char_id):
#     print('\n\nbruhhhhhh\n\n')
#     try:
#         character = Character.objects.get(id=char_id)
#         # print(character)
#     except request.DoesNotExist:
#         raise Http404()

#     if request.method == 'PUT':
#         # TODO: implementar
#         char = Character.objects.get(id=char_id)
#         new_char = request.data
#         char.name = new_char['nome']
#         char.race = new_char['raca']
#         char.playerClass = new_char['classe']
#         char.save()

#     elif request.method == 'DELETE':
#         # TODO: implementar
#         print("oI")

#     serialized_sheet = CharSerializer(character)
#     return Response(serialized_sheet.data)