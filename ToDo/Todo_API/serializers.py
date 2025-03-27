
from rest_framework import serializers
from .models import ToDos, UserToDo
from django.contrib.auth.hashers import make_password
class ToDoSerializer(serializers.ModelSerializer):
    # usertodo = serializers.PrimaryKeyRelatedField(queryset = UserToDo.objects.all(), write_only = True)
    # usertodo_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = ToDos
        fields =[ 'id', 'title','description', 'done']

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToDo
        fields = [
            'email', 
            'password'
        ]


class RegistrationUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserToDo
        fields = ['name', 'password', 'email',]
    
    
    def create(self, validated_data):
        
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)