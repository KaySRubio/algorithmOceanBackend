from rest_framework import serializers
from .models import Practice
from .models import Assignment
from .models import CustomUser #new
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer): #new
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username', 'password', 'accountType', 'classCode', 'last_login', 'date_joined', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}} # new

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user    
    #def save(self, commit=True):
    #    print('CustomUser serializer save method is running with self: ', self)

class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = ('id', 'email', 'algorithm', 'type', 'score')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 'email', 'question', 'score', 'weight')