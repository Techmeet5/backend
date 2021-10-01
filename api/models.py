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


class Test(models.Model):
    name     = models.CharField(max_length=40)
    gender   = models.CharField(max_length=40)

    def __str__(self):
        return 'Yo Yo {} {}'.format(self.name,self.gender)
