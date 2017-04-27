from django.shortcuts import render
from .models import Flight
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    flights_by_departure = Flight.objects.all()
    context = {
        'flights':flights_by_departure,
    }
    return render(request, 'flylo/index.html', context)

""" 
def flights(request,departure):
    flights_by_departure = Flight.objects.filter(location_departure=departure)
    context = {
        'flights':flights_by_departure,
        'departure':departure,
    }
    return render(request, 'flylo/flights.html', context)
"""

def flights2(request):
    selectedDeptarture = request.POST["d"]
    flights_by_departure = Flight.objects.filter(location_departure=selectedDeptarture)
    context = {
        'flights':flights_by_departure,
        'departure':selectedDeptarture,
    }
    return render(request, 'flylo/flights3.html', context)

def shoppingcart(request):
  selectedFlights =[]
  for key in request.POST:
     if key.startswith("checkbox") :
        selectedFlights.append(request.POST[key])
  request.session["selectedFligths"] = selectedFlights
  return HttpResponseRedirect(reverse('flylo:buy'))

def buy(request):
    flights_selected = Flight.objects.filter(pk__in=request.session["selectedFligths"])
    context = {
        'flights':flights_selected,
    }
    return render(request, 'flylo/buy.html', context)