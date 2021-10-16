#from django.db import models
from django.db.models.fields import EmailField

from djongo import models
from django import forms


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


# Details of every user
class MeetingDetails(models.Model):
    
    name     = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    email    = models.CharField(max_length=40)

    class Meta:
        abstract = True 

class MeetingDetailsForm(forms.ModelForm):

    class Meta:
        model = MeetingDetails
        fields = (
            'name', 'username', 'email'
        )

class Meetings(models.Model):
    room_name     = models.CharField(max_length=40)
    start_time    = models.CharField(max_length=40)
    end_time      = models.CharField(max_length=40)

    participant_1 = models.EmbeddedField( model_container = MeetingDetails, model_form_class=MeetingDetailsForm )
    """ participant_2 = models.EmbeddedField( model_container = MeetingDetails, model_form_class=MeetingDetailsForm )
    participant_3 = models.EmbeddedField( model_container = MeetingDetails, model_form_class=MeetingDetailsForm )
    participant_4 = models.EmbeddedField( model_container = MeetingDetails, model_form_class=MeetingDetailsForm )  """

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.room_name, self.start_time, self.end_time, self.participant_1, self.participant_2, self.participant_3, self.participant_4)




