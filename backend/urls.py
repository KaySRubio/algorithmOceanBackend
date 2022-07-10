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
router.register(r'customusers', views.CustomUser, 'CustomUser')
#router.register(r'practice', views.getpracticescores, 'Practice')

# new - digital ocean
router.register(r'practices', views.PracticeView, 'practice')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('csrf/', views.csrf),
    path('authenticateUser/', views.authenticateUser),
    path('getpracticescores/', views.getpracticescores),
    path('postpracticescore/', views.postpracticescore),
    path('api/', include(router.urls)), # new - digital ocean
]
