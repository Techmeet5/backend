#from django.db import models
from collections import defaultdict
from django.db.models.fields import EmailField

from djongo import models
from django import forms


# Create your models here.
class User(models.Model):
    username    = models.CharField(max_length=40, default="null",primary_key = True)
    email       = models.EmailField()
    first_name  = models.CharField(max_length=40)
    last_name   = models.CharField(max_length=40)
    college     = models.CharField(max_length=40, default="null")
    year        = models.IntegerField(default=2021)
    degree      = models.IntegerField(default=2)
    country     = models.CharField(max_length=40, default="null")
    password    = models.CharField(max_length=40, default="")
    about       = models.TextField(default="null")

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.username,self.email,self.first_name,self.last_name,self.college,self.year,self.degree,self.country,self.about)


# Details of every user
class MeetingDetails(models.Model):
    
    name     = models.CharField(max_length=40, default="none")
    username = models.CharField(max_length=40, default="none")
    email    = models.CharField(max_length=40, default="none@gmail.com")

    class Meta:
        abstract = True 


class Meetings(models.Model):
    room_name     = models.CharField(max_length=40)
    start_time    = models.CharField(max_length=40)
    end_time      = models.CharField(max_length=40)
    meet_url      = models.CharField(max_length=10)
    board_url     = models.CharField(max_length=10)
    """     participant_1 = models.EmbeddedField( model_container = MeetingDetails, null=True)
    participant_2 = models.EmbeddedField( model_container = MeetingDetails, null=True)
    participant_3 = models.EmbeddedField( model_container = MeetingDetails, null=True)
    participant_4 = models.EmbeddedField( model_container = MeetingDetails, null=True) """

    host          = models.CharField(max_length=40)
    host_name     = models.CharField(max_length=40)
    host_email    = models.CharField(max_length=40)

    participant_2          = models.CharField(max_length=40)
    participant_2_name     = models.CharField(max_length=40)
    participant_2_email    = models.CharField(max_length=40)

    participant_3          = models.CharField(max_length=40)
    participant_3_name     = models.CharField(max_length=40)
    participant_3_email    = models.CharField(max_length=40)

    participant_4          = models.CharField(max_length=40)
    participant_4_name     = models.CharField(max_length=40)
    participant_4_email    = models.CharField(max_length=40)

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.room_name, self.start_time, self.end_time, self.host, self.participant_2, self.participant_3, self.participant_4)




