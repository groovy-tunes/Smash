from django.db import models
from django.contrib.auth.models import User
from vote.managers import VotableManager
from django.utils import timezone
import math

class Post(models.Model):
    user = models.ForeignKey(User, default=0)
    body = models.TextField()
    time = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    votes = VotableManager()
    vote_count = models.IntegerField(default=0)

    def formatTime(self):
        seconds_value = self.time % 60
        seconds = str(seconds_value)
        if seconds_value < 10:
            seconds = "0" + str(seconds_value)
        minutes = math.floor(self.time/60)
        return "{}:{}".format(str(minutes),seconds)

    def __str__(self):
        return self.user.username + str(self.pk)

class Vod(models.Model):
    user = models.ForeignKey(User, default=0)
    url = models.URLField(default='')
    title = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    posts = models.ManyToManyField(Post)
    #tags = models.TextField(max_length=100, default='')
    
    def __str__(self):
        return self.user.username + str(self.pk)

