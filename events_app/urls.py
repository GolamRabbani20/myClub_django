from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('<int:year>/<str:month>', views.Home, name='home'),

    path('add_venue/', views.addVenue, name='add-venue'),
    path('list_venue/', views.listVenues, name='list-venues'),
    path('show_venue/<venue_id>', views.showVenue, name='show-venue'),
    path('update_venue/<venue_id>', views.updateVenue, name='update-venue'),
    path('delete_venue/<venue_id>', views.deleteVenue, name='delete-venue'),
    path('venue_text/', views.venueText, name='venue-text'),
    path('indivisual_veneue_text/<venue_id>', views.indivisualVenueText, name='indivisual-venue-text'),
    path('venue_csv/', views.venueCSV, name='venue-csv'),
    path('indivisual_venue_csv/<venue_id>', views.indivisualVenueCSV, name='indivisual-venue-csv'),
    path('venue_pdf/', views.venuePDF, name='venue-pdf'),
    path('indivisual_veneue_pdf/<venue_id>', views.indivisualVenuePDF, name='indivisual-venue-pdf'),

    path('list_events/', views.listEvents, name='list-events'),
    path('add_event/', views.addEvent, name='add-event'),
    path('update_event/<event_id>', views.updateEvent, name='update-event'),
    path('delete_event/<event_id>', views.deleteEvent, name='delete-event'),

]
