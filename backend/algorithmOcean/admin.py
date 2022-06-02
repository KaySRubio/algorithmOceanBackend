from django.contrib import admin

# Register your models here.
from .models import Account
from .models import Practice
from .models import Assignment

class AccountAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'password', 'accountType', 'classCode')

class PracticeAdmin(admin.ModelAdmin):
    list_display = ('email', 'algorithm', 'type', 'score')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('email', 'assignment', 'question', 'score', 'weight')

# Register your models here.

admin.site.register(Account, AccountAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(Assignment, AssignmentAdmin)