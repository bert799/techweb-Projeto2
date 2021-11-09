from rest_framework import serializers
from .models import Character

class CharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'race', 'playerClass']