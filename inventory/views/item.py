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

templater = get_renderer('inventory')

######################################################
###  Shows the list of items
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def process_request(request):
  params = {}

  items = hmod.Item.objects.all().order_by('name')

  params['items'] = items

  return templater.render_to_response(request, 'item.html', params)

######################################################
###  Edit a items
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def edit(request):
  params = {}

  try:
    item = hmod.Item.objects.get(id=request.urlparams[0])
  except hmod.Item.DoesNotExist:
    return HttpResponseRedirect('/inventory/item/')

  form = ItemEditForm(initial={
    'name': item.name,
    'description': item.description,
    'value': item.value,
    'standard_rental_price': item.standard_rental_price,
    #user (owner)
  })
  if request.method == 'POST':
    form = ItemEditForm(request.POST)
    form.itemid = item.id
    if form.is_valid():
      item.name = form.cleaned_data['name']
      item.description = form.cleaned_data['description']
      item.value = form.cleaned_data['value']
      item.standard_rental_price = form.cleaned_data['standard_rental_price']
      item.save()
      return HttpResponseRedirect('/inventory/item/')      


  params['form'] = form
  params['items'] = item

  return templater.render_to_response(request, 'item.edit.html', params)

class ItemEditForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100)
  description = forms.CharField(label='Description', required=True, max_length=100)
  value = forms.CharField(label='Value', required=True)
  standard_rental_price = forms.CharField(label='Standard Rental Price')
  #user (owner)

  def clean_name(self):
    item_count = hmod.Item.objects.filter(name=self.cleaned_data['name']).exclude(id=self.itemid).count() #self aka (this) calls form.itemid because this section of the area is IN the form
    if item_count >= 1:
      raise forms.ValidationError("It seems we already have a item entered under this name.  Please verify and try again.")
    return self.cleaned_data['name']

######################################################
###  Creates a new item
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def create(request):
  # params = {}

  item = hmod.Item()
  item.name = ''
  item.description = ''
  item.value = None
  item.standard_rental_price = None
  item.save()

  return HttpResponseRedirect('/inventory/item.edit/{}'.format(item.id))

######################################################
###  Deletes a new item
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def delete(request):
  try:
    item = hmod.Item.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/inventory/item/')
  item.delete()
  return HttpResponseRedirect('/inventory/item/')

######################################################
###  Deletes a new item
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def management(request):
  params = {}

  items = hmod.Item.objects.all().order_by('name')

  params['items'] = items

  return templater.render_to_response(request, 'item.management.html', params)
