from django.contrib import admin

from.models import Word
# Register your models her


class WordModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'mean', 'modify_date')
    ordering = ('-modify_date',)
    readlonly_fields = ('id', 'modify_date')


admin.site.register(Word, WordModelAdmin)
