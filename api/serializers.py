from .models import Test, User
from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['name','gender']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','college','year','degree','country','about']
        