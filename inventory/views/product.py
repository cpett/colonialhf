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
@permission_required('homepage.change_user', login_url='/homepage/login/')
def process_request(request):
  params = {}

  products = hmod.Product.objects.all().order_by('name')

  params['products'] = products

  return templater.render_to_response(request, 'product.html', params)

######################################################
###  Edit a products
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def edit(request):
  params = {}

  try:
    product = hmod.Product.objects.get(id=request.urlparams[0])
  except hmod.Product.DoesNotExist:
    return HttpResponseRedirect('/inventory/product/')

  form = productEditForm(initial={
    'name': product.name,
    'description': product.description,
    'category': product.category,
    'current_price': product.current_price,
    #user (owner)
  })
  if request.method == 'POST':
    form = productEditForm(request.POST)
    form.productid = product.id
    if form.is_valid():
      product.name = form.cleaned_data['name']
      product.description = form.cleaned_data['description']
      product.category = form.cleaned_data['category']
      product.current_price = form.cleaned_data['current_price']
      product.save()
      return HttpResponseRedirect('/inventory/product/')      


  params['form'] = form
  params['products'] = product

  return templater.render_to_response(request, 'product.edit.html', params)

class productEditForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100)
  description = forms.CharField(label='Description', required=True, max_length=100)
  category = forms.CharField()
  current_price = forms.CharField(label='Current Price')
  #user (owner)

  def clean_name(self):
    product_count = hmod.Product.objects.filter(name=self.cleaned_data['name']).exclude(id=self.productid).count() #self aka (this) calls form.productid because this section of the area is IN the form
    if product_count >= 1:
      raise forms.ValidationError("It seems we already have a product entered under this name.  Please verify and try again.")
    return self.cleaned_data['name']

######################################################
###  Creates a new product
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
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
@permission_required('homepage.change_user', login_url='/homepage/login/')
def delete(request):
  try:
    product = hmod.Product.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/inventory/product/')
  product.delete()
  return HttpResponseRedirect('/inventory/product/')