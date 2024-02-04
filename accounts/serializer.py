
from rest_framework import serializers
from .models import User  # Corrected import statement

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']
