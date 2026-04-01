from rest_framework import serializers
from api.models import Edition

class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ['id', 'title', 'description', 'place', 'date', 'portrait']