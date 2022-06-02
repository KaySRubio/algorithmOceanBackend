from rest_framework import serializers
from .models import Account
from .models import Practice
from .models import Assignment

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