from rest_framework import serializers
from .models import Race

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['name', 'slug', 'desc', 'asi_desc', 'asi','age', 'alignment', 'size', 'speed','speed_desc', 'languages', 'vision', 'traits', 'subraces','document_slug', 'document_title', 'document_license_url']