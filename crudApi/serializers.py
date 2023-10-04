from rest_framework import serializers
from .models import ModifiedUser

class ModifiedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModifiedUser
        fields = ('id', 'email', 'name', 'is_active',  'is_staff', 'is_superuser','date_joined')