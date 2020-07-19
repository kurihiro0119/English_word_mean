from rest_framework import serializers
from .models import Word
from .english_word import get_mean_word
import json


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ['word', 'mean']


class GetWordsSerializer(serializers.Serializer):

    word = serializers.CharField()
    mean = serializers.SerializerMethodField()

    def get_mean(self, obj):
        if obj['word'] is None:
            return None
        mean = get_mean_word(obj['word'])
        return mean


class WordSerializerField(serializers.Field):

    mean = None

    def to_value(self, data):
        self.mean = get_mean_word(data.word)
        return self.mean


class MyWordSerializer(serializers.ModelSerializer):
    mean = serializers.SerializerMethodField()
    # mean = WordSerializerField()

    class Meta:
        model = Word
        fields = ['word', 'mean']

    def get_mean(self, obj):
        if obj.word is None:
            return None
        mean = get_mean_word(obj.word)
        return mean

    # def is_named_bar(self, word):
    #     mean = get_mean_word(word.word)
    #     return mean
