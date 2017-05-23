from django.db import models
from vote.models import VoteModel

class Suggestion(VoteModel, models.Model):
  suggestion_text = models.CharField(max_length=500)
  pub_date = models.DateTimeField('date published')
