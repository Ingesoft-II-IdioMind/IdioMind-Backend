from .models import UserAccount
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'last_name','native_idiom','is_active','is_staff']
        read_only_fields = ['id', 'email','is_active','is_staff']