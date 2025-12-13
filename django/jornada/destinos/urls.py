from django.urls import path
from . import views
urlpatterns = [
    path('', views.destinos, name='destinos'),
]