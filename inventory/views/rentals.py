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
###  Shows the list of products
@view_function
def process_request(request):
  params = {}
  
  items = hmod.Item.objects.all().order_by('name')

  params['items'] = items

  return templater.render_to_response(request, 'rentals.html', params)

######################################################
###  
@view_function
def details(request):
  params = {}

  try:
    product = hmod.Item.objects.get(id=request.urlparams[0])
  except hmod.Product.DoesNotExist:
    return HttpResponseRedirect('/inventory/store/')

  form = productEditForm(initial={
    'name': product.name,
    'description': product.description,
    'value': product.value,
    'standard_rental_price': product.standard_rental_price,
    #user (owner)
  })

  params['form'] = form
  params['product'] = product

  return templater.render_to_response(request, 'rentals.details.html', params)

class productEditForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100)
  description = forms.CharField(label='Description', required=True, max_length=100)
  value = forms.CharField()
  standard_rental_price = forms.CharField(label='Rental Price')
  #user (owner)

  def clean_name(self):
    product_count = hmod.Product.objects.filter(name=self.cleaned_data['name']).exclude(id=self.productid).count() #self aka (this) calls form.productid because this section of the area is IN the form
    if product_count >= 1:
      raise forms.ValidationError("It seems we already have a product entered under this name.  Please verify and try again.")
    return self.cleaned_data['name']

######################################################
###  Creates a new product
@view_function
def create(request):
  # params = {}

  product = hmod.Product()
  product.name = ''
  product.description = ''
  product.category = ''
  product.current_price = None
  product.save()

  return HttpResponseRedirect('/inventory/product.edit/{}'.format(product.id))

######################################################
###  Deletes a new product
@view_function
def delete(request):
  try:
    product = hmod.Product.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/inventory/product/')
  product.delete()
  return HttpResponseRedirect('/inventory/product/')


