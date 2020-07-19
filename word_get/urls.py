from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('word', views.WordViewSet)

app_name = 'word_get'
urlpatterns = [
    path('', include(router.urls)),
    path('get/', views.GetWordViewSet.as_view()),
    path('save/', views.MyWordViewSet.as_view()),
]
