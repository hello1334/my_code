from django.urls import path
from . import views

app_name='myapp'
urlpatterns = [
    path('', views.index),
    path('example/', views.example),
]