from rest_framework import serializers
from .models import Word
from .english_word import get_mean_word
import json


class GetWordsSerializer(serializers.Serializer):

    word = serializers.CharField()
    mean = serializers.SerializerMethodField()

    def get_mean(self, obj):
        if obj['word'] is None:
            return None
        mean = get_mean_word(obj['word'])
        return mean
