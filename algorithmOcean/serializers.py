from rest_framework import serializers
from .models import Account
from .models import Practice
from .models import Assignment
from .models import CustomUser #new

class UserSerializer(serializers.ModelSerializer): #new
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username', 'password', 'accountType', 'classCode', 'last_login', 'date_joined', 'is_staff')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'firstname', 'lastname', 'email', 'password', 'accountType', 'classCode')

class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = ('id', 'email', 'algorithm', 'type', 'score')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 'email', 'question', 'score', 'weight')