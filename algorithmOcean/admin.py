from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .serializers import UserSerializer # new

# Register your models here.
from .models import Practice
from .models import Assignment
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'username', 'password', 'accountType', 'classCode']

class PracticeAdmin(admin.ModelAdmin):
    list_display = ('email', 'algorithm', 'type', 'score')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('email', 'assignment', 'question', 'score', 'weight')

# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(Assignment, AssignmentAdmin)