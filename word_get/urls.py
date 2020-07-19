from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'word_get'
urlpatterns = [
    path('get/', views.GetWordViewSet.as_view()),
]
