import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    text = models.CharField(max_length=120)
    publishedDate = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.text

    def wasPublishedRecently(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publishedDate <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.text

