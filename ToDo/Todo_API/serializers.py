
from rest_framework import serializers
from .models import ToDos, UserToDo
from django.contrib.auth.hashers import make_password
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDos
        fields = '__all__'

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToDo
        fields = [
            'email', 
            'password'
        ]


class RegistrationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToDo
        fields = ['name', 'password', 'email',]
    
    
    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)