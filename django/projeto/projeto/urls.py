"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from http.client import HTTPResponse
from django.contrib import admin
from django.urls import path
from blog import views as view_blog
from home import views as view_home
from contato import views as view_contato
#from projeto.views import home
#funçoes para carregar views diretamente
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view_home.home),
    path('home/',view_home.home),
    path('blog/',view_blog.blog),
    path('contato/',view_contato.contato),
]
