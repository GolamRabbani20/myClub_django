from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField('Venue Aame', max_length=101)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=20)
    phone = models.CharField('Contact Phone', max_length=20)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address')
    
    def __str__(self):
        return self.name
class MyClubUser(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120, null=False, blank=False)
    event_date = models.DateTimeField('Event date' )
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
