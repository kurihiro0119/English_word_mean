from rest_framework import viewsets
from rest_framework import views, status
from rest_framework.response import Response
# Create your views here.
from .models import Word
from .serializers import GetWordsSerializer
from .english_word import get_mean_word
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser


class GetWordViewSet(views.APIView):

    def post(self, request, *args, **kwargs):

        serializer = GetWordsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)
