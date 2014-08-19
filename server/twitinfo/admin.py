from twitinfo.models import Event
from twitinfo.models import Keyword
from twitinfo.models import Tweet
from twitinfo.models import WordFrequency
from django.contrib import admin

admin.site.register(Event)
admin.site.register(Keyword)
admin.site.register(Tweet)
admin.site.register(WordFrequency)
