from __future__ import unicode_literals
from django.db import models


class Topic(models.Model):

    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'topics'

    def __unicode__(self):
        return self.name


class Location(models.Model):

    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        unique_together = ('city', 'country', 'state',)
        verbose_name_plural = 'locations'

    def __unicode__(self):
        return ", ".join([self.city, self.country, self.state])


class Event(models.Model):

    topic = models.ForeignKey(Topic)
    location = models.ForeignKey(Location)
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'events'

    def __unicode__(self):
        return self.name
