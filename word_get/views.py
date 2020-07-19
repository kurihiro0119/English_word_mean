from rest_framework import viewsets
from rest_framework import views, status
from rest_framework.response import Response
# Create your views here.
from .models import Word
from .serializers import WordSerializer, GetWordsSerializer, MyWordSerializer
from .english_word import get_mean_word
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser


class WordViewSet(viewsets.ModelViewSet):

    queryset = Word.objects.all()
    serializer_class = WordSerializer


# class WordFilter(filters.FilterSet):
#     class Meta:
#         model = Word
#         fields = ['word', 'mean']


class GetWordViewSet(views.APIView):

    def post(self, request, *args, **kwargs):

        # 辞書型になってるからブッ込めばいい？

        serializer = GetWordsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)

    #     serializer = MyWordSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)
    # queryset = Word.objects.all()
    # serializer_class = MyWordSerializer


class MyWordViewSet(views.APIView):

    def post(self, request, *args, **kwargs):

        # 辞書型になってるからブッ込めばいい？

        serializer = MyWordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
