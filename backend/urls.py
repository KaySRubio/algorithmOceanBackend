"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from algorithmOcean import views
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'accounts', views.Account, 'Account')
router.register(r'customusers', views.CustomUser, 'CustomUser')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    #path('accounts/', include('django.contrib.auth.urls')), #new
    #path('accounts/login/', views.login), #new
    path('accounts/login/', auth_views.LoginView.as_view()),

    #path('auth/', include('rest_auth.urls')),    
    #path('auth/register/', include('rest_auth.registration.urls')),


    #path('api/v1/users/', include('users.urls')),


    path('csrf/', views.csrf),
    path('authenticateUser/', views.authenticateUser),
    path('help/', views.help),
    path("db/", views.db, name="db"),
]
