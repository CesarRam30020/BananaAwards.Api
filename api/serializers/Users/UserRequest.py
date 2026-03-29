from rest_framework import serializers
from api.models import User

class UserRequest(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']