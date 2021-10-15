from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class User(models.Model):
    username    = models.CharField(max_length=40, default="null")
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


class Meetings(models.Model):
    room_name     = models.CharField(max_length=40)
    start_time    = models.CharField(max_length=40)
    end_time      = models.CharField(max_length=40)
    participant_1 = models.CharField(max_length=40)
    participant_2 = models.CharField(max_length=40)
    participant_3 = models.CharField(max_length=40)
    participant_4 = models.CharField(max_length=40)

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.room_name, self.start_time, self.end_time, self.participant_1, self.participant_2, self.participant_3, self.participant_4)

