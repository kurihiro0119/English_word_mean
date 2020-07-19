import uuid

from django.db import models
from django.utils import timezone
from .english_word import get_mean_word

# Create your models here.


class Word(models.Model):

    class Meta:
        db_table = 'word'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(verbose_name='Word', max_length=20)
    mean = models.CharField(verbose_name='Mean', max_length=200)
    modify_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.mean

    def get_word_mean(self):
        return get_mean_word(self.word)
