from django.shortcuts import render
from .models import Flight
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from itertools import chain

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
    if request.POST:
      selectedDeparture = request.POST["d"]
      flights_by_departure = Flight.objects.filter(location_departure=selectedDeparture)
      context = {
          'flights':flights_by_departure,
          
      }
      request.session["selectedDeparture"] = selectedDeparture


    return render(request, 'flylo/flights3.html', context)

def shoppingcart(request):
  selectedFlights =[]
  selected_to_return=[] #Llista de vols que volem tornada
  totalFlights=[]
  returnFlights=[]
  for key in request.POST:
     if key.startswith("checkbox") :
        selectedFlights.append(request.POST[key])
        
     if key.startswith("ret") :
        selected_to_return.append(request.POST[key])
  request.session["selectedFligths"] = selectedFlights
  

  totalFlights = Flight.objects.filter(pk__in=selectedFlights)
  for departure in Flight.objects.values_list("location_arrival", flat=True).filter(pk__in=selected_to_return):
    for flight in Flight.objects.filter(location_departure=departure).filter(location_arrival=request.session["selectedDeparture"]):
      returnFlights.append(flight)
  result_list = list(chain(totalFlights,returnFlights))
  print returnFlights
  context = {
        'flights':result_list,
        'returnflights':returnFlights,
  }
  if not selected_to_return: #Si no hi ha res a la llista de return va a buy 
    return HttpResponseRedirect(reverse('flylo:buy'),context)
  else:
    return render(request, 'flylo/flights3.html', context) # si hi va a tornada per selecciona vols
    
    
    
    
  

def buy(request):
    flights_selected = Flight.objects.filter(pk__in=request.session["selectedFligths"])
    context = {
        'flights':flights_selected,
    }
    return render(request, 'flylo/buy.html', context)