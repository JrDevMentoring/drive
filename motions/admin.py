from django.contrib import admin

from .models import Suggestion
from django_slack_oauth.models import SlackUser

admin.site.register(Suggestion)
admin.site.register(SlackUser)
