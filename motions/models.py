from django.db import models

class Suggestion(models.Model):
  suggestion_text = models.CharField(max_length=500)
  votes = models.IntegerField(default=0)
  pub_date = models.DateTimeField('date published')
