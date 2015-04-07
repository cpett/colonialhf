from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin import widgets
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType

templater = get_renderer('events')

######################################################
###  Shows the list of events
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def process_request(request):
  params = {}

  events = hmod.Event.objects.all().order_by('start_date')

  params['events'] = events

  return templater.render_to_response(request, 'event.html', params)

######################################################
###  Edit a events
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def edit(request):
  params = {}

  try:
    event = hmod.Event.objects.get(id=request.urlparams[0])
  except hmod.Event.DoesNotExist:
    return HttpResponseRedirect('/events/event/')

  form = EventEditForm(initial={
    'name': event.name,
    'start_date': event.start_date,
    'map_file_name': event.map_file_name,
  })
  if request.method == 'POST':
    form = EventEditForm(request.POST)
    form.eventid = event.id
    if form.is_valid():
      event.name = form.cleaned_data['name']
      event.start_date = form.cleaned_data['start_date']
      event.map_file_name = form.cleaned_data['map_file_name']
      event.save()
      return HttpResponseRedirect('/events/event/')      


  params['form'] = form
  params['events'] = event

  return templater.render_to_response(request, 'event.edit.html', params)

class EventEditForm(forms.Form):
  name = forms.CharField(label='Name')
  start_date = forms.DateField(widget = widgets.AdminDateWidget)
  map_file_name = forms.CharField(label='Map File Name', required=True, max_length=100)
  #eventid from form.eventid = event.id

  def clean_name(self):
    event_count = hmod.Event.objects.filter(name=self.cleaned_data['name']).exclude(id=self.eventid).count() #self aka (this) calls form.eventid because this section of the area is IN the form
    if event_count >= 1:
      raise forms.ValidationError("We already have an event with that name.  Please check the name and try again.")
    return self.cleaned_data['name']

######################################################
###  Creates a new event
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def create(request):
  # params = {}

  event = hmod.Event()
  event.name = ''
  event.start_date = None
  event.map = ''
  event.save()

  return HttpResponseRedirect('/events/event.edit/{}'.format(event.id))

######################################################
###  Deletes a new event
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def delete(request):
  try:
    event = hmod.Event.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/events/event/')
  event.delete()
  return HttpResponseRedirect('/events/event/')

######################################################
###  Shows the list of events
@view_function
def view(request):
  params = {}

  events = hmod.Event.objects.all().order_by('start_date')

  params['events'] = events

  return templater.render_to_response(request, 'event.view.html', params)

@view_function
def details(request):
  params = {}

  events = hmod.Event.objects.all().filter(id=request.urlparams[0])
  products = hmod.Product.objects.all()

  params['events'] = events
  params['products'] = products
  return templater.render_to_response(request, 'event.details.html', params)