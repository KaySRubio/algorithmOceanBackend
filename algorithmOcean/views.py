from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccountSerializer, UserSerializer
#from .models import Account, CustomUser
from .models import CustomUser as CustomUserModel
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect 
from django.contrib.auth import authenticate
import json 
from django.core import serializers

# Create your views here.
#@method_decorator(csrf_exempt, name='dispatch')
#@ensure_csrf_cookie
#class Account(viewsets.ModelViewSet):
#    serializer_class = AccountSerializer
#    queryset = Account.objects.all()


#@method_decorator(csrf_exempt, name='dispatch')
#@ensure_csrf_cookie
@method_decorator(ensure_csrf_cookie, name='dispatch')
class CustomUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUserModel.objects.all()

#@method_decorator(ensure_csrf_cookie, name='dispatch')
#def csrf(request):
#    return JsonResponse({'csrfToken': get_token(request)})

@ensure_csrf_cookie
def csrf(request):
    # request.set_cookie("testing","testing_token",samesite="None") # set_cookie isn't working
    csrf_token = request.META.get('CSRF_COOKIE')
    return JsonResponse({'result': csrf_token})
    #return csrf_token

#@csrf_exempt
def login(request):
    return JsonResponse({'result': 'OK'})

def authenticateUser(request):
    credentials = str(request.body).split(',') # put the request.body in a string and split into array
    username8 = credentials[0].replace('b\"username=', '').replace("\'", "")
    password8 = credentials[1].replace('password=', '').replace("\'", "").replace(" ", "").replace('\"', "")
    user = authenticate(username=username8, password=password8)
    if user is not None:
        person = CustomUserModel.objects.get(username=username8)
        account = {}
        account["username"] = person.username
        account["first_name"] = person.first_name
        account["last_name"] = person.last_name
        account["is_active"] = person.is_active
        account["accountType"] = person.accountType
        account["classCode"] = person.classCode
        print(person.username, 'logged in')
        return JsonResponse({'result': account})
    else:
        print('not logged in')
        return JsonResponse({'result': 'NOT logged in'})

def help(request):
    print(request.META)
    request.META["CSRF_COOKIE_USED"] = True
    return JsonResponse({'result': 'OK'})

def db(request):
    customUser = CustomUser()
    # customUser.save()
    # customUsers = CustomUser.objects.all()
    return render(request, "db.html", {"customUsers": customUser})
