from django.db import models


class SlackTeam(models.Model):
    name = models.CharField(max_length=64)
    token = models.CharField(max_length=64)


class SlackBot(models.Model):
    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=64)
    team = models.ForeignKey(SlackTeam, related_name='bots')
