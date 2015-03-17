from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin import widgets
from homepage.State import State
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType

templater = get_renderer('events')

######################################################
###  Shows the list of venues
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def process_request(request):
  params = {}

  venues = hmod.Venue.objects.all().order_by('name')

  params['venues'] = venues

  return templater.render_to_response(request, 'venue.html', params)

######################################################
###  Edit a venues
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def edit(request):
  params = {}

  try:
    venue = hmod.Venue.objects.get(id=request.urlparams[0])
  except hmod.Venue.DoesNotExist:
    return HttpResponseRedirect('/events/venue/')

  form = VenueEditForm(initial={
    'name': venue.name,
    'address': venue.address,
    'city': venue.city,
    'state': venue.state,
    'zip': venue.zip,
  })
  if request.method == 'POST':
    form = VenueEditForm(request.POST)
    form.venueid = venue.id
    if form.is_valid():
      venue.name = form.cleaned_data['name']
      venue.address = form.cleaned_data['address']
      venue.city = form.cleaned_data['city']
      venue.state = form.cleaned_data['state']
      venue.save()
      return HttpResponseRedirect('/events/venue/')      


  params['form'] = form
  params['venues'] = venue

  return templater.render_to_response(request, 'venue.edit.html', params)

class VenueEditForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100)
  address = forms.CharField(label='Address', required=True, max_length=100)
  city = forms.CharField(label='City', required=True, max_length=100)
  state = forms.ChoiceField(State.STATE_CHOICES)
  zip = forms.CharField(label='ZIP', required=True, max_length=100)

  def clean_name(self):
    venue_count = hmod.Venue.objects.filter(name=self.cleaned_data['name']).exclude(id=self.venueid).count() #self aka (this) calls form.venueid because this section of the area is IN the form
    if venue_count >= 1:
      raise forms.ValidationError("It seems we already have a venue entered under this name.  Please verify and try again.")
    return self.cleaned_data['name']

######################################################
###  Creates a new venue
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def create(request):
  # params = {}

  venue = hmod.Venue()
  venue.name = ''
  venue.address = ''
  venue.city = ''
  venue.state = ''
  venue.zip = None
  venue.save()

  return HttpResponseRedirect('/events/venue.edit/{}'.format(venue.id))

######################################################
###  Deletes a new venue
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def delete(request):
  try:
    venue = hmod.Venue.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/events/venue/')
  venue.delete()
  return HttpResponseRedirect('/events/venue/')