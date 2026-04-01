from rest_framework import serializers
from api.models import Edition

class EditionRequest(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ['title', 'description', 'place', 'date', 'portrait']