from __future__ import unicode_literals

from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=8)
    estimated_time_departure =  models.DateTimeField()
    estimated_time_arrival =  models.DateTimeField()
    location_departure =  models.CharField(max_length=3)
    location_arrival = models.CharField(max_length=3)
    airline = models.CharField(max_length=3)
    aircraft = models.CharField(max_length=4)
    status = models.CharField(max_length=40)
    def __str__(self):
        return "["+self.flight_number+"] "+ self.location_departure +"-"+ self.location_arrival + " : "+ str(self.estimated_time_departure) + " / " + str(self.estimated_time_arrival) + " ["+ self.status +"]"


class Airline(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Airplane(models.Model):
    model = models.CharField(max_length=40)
    reference_code = models.CharField(max_length=100)
    number_seats_tourist = models.CharField(max_length=5)
    number_seats_business = models.CharField(max_length=5)
    number_seats_excellence = models.CharField(max_length=5)
    category = models.ForeignKey(Airline, on_delete=models.CASCADE)
    def __str__(self):
        return "["+self.model+"] "+self.reference_code