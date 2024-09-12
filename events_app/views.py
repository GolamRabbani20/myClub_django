from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime as dt
from .models import Event, Venue, MyClubUser
from .forms import VenueForm, EventForm
from django.http import  HttpResponseRedirect, FileResponse
from django.contrib import messages
from django.http import HttpResponse
import csv

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io

from django.core.paginator import Paginator

# -------------------------------------------------------------------->| Venues Download |<---------------------------------------------------------------
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

def venueCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attatchment; filename=venue.csv'

    writer = csv.writer(response)
    venues = Venue.objects.all()
    #Heading
    writer.writerow(['Venue-name', 'Address', 'Zip_code', 'Phone', 'Web-address', 'Email_address'])

    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])
    
    return response

def indivisualVenueCSV(request, venue_id):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attatchment; filemane = venue.csv'

    writer = csv.writer(response)
    venue = Venue.objects.get(pk = venue_id)

    writer.writerow(['Venue-name', 'Address', 'Zip_code', 'Phone', 'Web-address', 'Email_address'])
    writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])

    return response

def venuePDF(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    #Create a canvas
    c = canvas.Canvas(buf, pagesize = letter, bottomup = 0)
    # Create a text object
    text_obj = c.beginText()
    text_obj.setTextOrigin(inch, inch)
    text_obj.setFont('Helvetica', 14)

    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append("--------------------------------------------------------")
  

    for line in lines:
        text_obj.textLine(line)

    c.drawText(text_obj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=venue.name +'_'+ str(venue.id) + '.pdf')


def indivisualVenuePDF(request, venue_id):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 16)

    venue = Venue.objects.get(pk=venue_id)
    lines = []
    lines.append(venue.name)
    lines.append(venue.address)
    lines.append(venue.zip_code)
    lines.append(venue.phone)
    lines.append(venue.web)
    lines.append(venue.email_address)

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename=venue.name +'.pdf')

# ------------------------------------------------------------------->| Events |<----------------------------------------------------------------------
def listEvents(request):
    all_events = Event.objects.all()
    p = Paginator(all_events, 1)
    page = request.GET.get('page')
    events = p.get_page(page)
    nums = 'a' * events.paginator.num_pages
    return render(request, 'events/list_events.html', {'events_number': len(all_events), 'events': events, 'nums': nums})

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
# ------------------------------------------------------------>| Venue |<----------------------------------------------------------------------------------
def listVenues(request):
    all_venues = Venue.objects.all()
    p = Paginator(all_venues, 5)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = 'a' * venues.paginator.num_pages
    return render(request, 'venues/list_venue.html', {'venues': venues, 'venues_number': len(all_venues), 'nums': nums})

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

def deleteVenue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

# --------------------------------------------------------------------------------->| Home Page |<-----------------------------------------------------------
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