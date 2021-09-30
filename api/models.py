from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class User(models.Model):
    username    = models.CharField(max_length=40)
    email       = models.EmailField()
    first_name  = models.CharField(max_length=40)
    last_name   = models.CharField(max_length=40)
    college     = models.CharField(max_length=40)
    year        = models.IntegerField()
    degree      = models.IntegerField()
    country     = models.CharField(max_length=40)
    about       = models.TextField()

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.username,self.email,self.first_name,self.last_name,self.college,self.year,self.degree,self.country,self.about)


class Test(models.Model):
    name     = models.CharField(max_length=40)
    gender   = models.CharField(max_length=40)

    def __str__(self):
        return 'Yo Yo {} {}'.format(self.name,self.gender)
