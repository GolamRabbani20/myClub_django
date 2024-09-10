from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime as dt
from .models import Event, Venue, MyClubUser
from .forms import VenueForm, EventForm
from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse

# -----------------------------------------------------------------------------------------------------------------------------------------------------
def venueText(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attatchment; filename=venue.txt'
    venues = Venue.objects.all()
    lines = []

    for venue in venues:
        lines.append('................................................\n')
        lines.append(f'{venue.name}\n {venue.address}\n {venue.zip_code}\n { venue.phone}\n {venue.web}\n { venue.email_address}\n')
        lines.append('................................................')
    response.writelines(lines)
    return response

def indivisualVenueText(request, venue_id):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attatchment; filename=venue.txt'
    venue = Venue.objects.get(pk=venue_id)
    lines = []

    lines.append('................................................\n')
    lines.append(f'{venue.name}\n {venue.address}\n {venue.zip_code}\n { venue.phone}\n {venue.web}\n { venue.email_address}\n')
    lines.append('................................................')
    response.writelines(lines)
    return response



# -----------------------------------------------------------------------------------------------------------------------------------------------------
def listEvents(request):
    all_events = Event.objects.all().order_by('-event_date')
    return render(request, 'events/list_events.html', {'all_events': all_events, 'events_number': len(all_events)})

def listVenues(request):
    all_venues = Venue.objects.all().order_by('pk')
    return render(request, 'venues/list_venue.html', {'all_venues': all_venues, 'venues_number': len(all_venues)})

def showVenue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'venues/show_venue.html', {'venue': venue})

def updateVenue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        # messages.success(request, 'Updated Successfully!!!')
        return redirect('list-venues')
    return render(request, 'venues/update_venue.html', {'venue': venue, 'form': form})

def updateEvent(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html', {'event':event, 'form': form})

def deleteEvent(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def deleteVenue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def addVenue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'venues/add_venue.html', {'form': form, 'submitted': submitted})

def addEvent(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
       form = EventForm()
       if 'submitted' in request.GET:
           submitted = True
    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})






def Home(request, month=dt.now().strftime("%B"), year=dt.now().year):
    name = 'Rabbani'
    month_number = [month.upper() for month in list(calendar.month_name)].index(month.upper())
    #Create calander 
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = dt.now()
    crrent_year = now.year
    current_time = now.strftime('%I: %M :%S: %p')
    return render(request, 'events/home.html', {
        'age': 2+23, 
        'name': name, 
        'month':month.capitalize(), 
        'year': year,
        'month_number': month_number,
        'cal': cal,
        'crrent_year': crrent_year,
        'current_time': current_time
    })