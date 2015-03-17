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
###  Shows the list of order
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def process_request(request):
  params = {}

  orders = hmod.Order.objects.all().order_by('order_date')

  params['orders'] = orders

  return templater.render_to_response(request, 'order.html', params)

######################################################
###  Edit a order
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def edit(request):
  params = {}

  try:
    order = hmod.Order.objects.get(id=request.urlparams[0])
  except hmod.Order.DoesNotExist:
    return HttpResponseRedirect('/inventory/order/')

  form = oderEditForm(initial={
    'order_date': order.order_date,
    'phone': order.phone,
    'date_picked': order.date_picked,
    'date_paid': order.date_paid,
    'date_shipped': order.date_shipped,
    'tracking_number': order.tracking_number,
    #user (owner)
  })
  if request.method == 'POST':
    form = oderEditForm(request.POST)
    form.oderid = order.id
    if form.is_valid():
      order.order_date = form.cleaned_data['order_date']
      order.phone = form.cleaned_data['phone']
      order.date_picked = form.cleaned_data['date_picked']
      order.date_paid = form.cleaned_data['date_paid']
      order.date_shipped = form.cleaned_data['date_shipped']
      order.tracking_number = form.cleaned_data['tracking_number']
      order.save()
      return HttpResponseRedirect('/inventory/order/')      


  params['form'] = form
  params['order'] = order

  return templater.render_to_response(request, 'order.edit.html', params)

class oderEditForm(forms.Form):
  order_date = forms.DateField(widget = widgets.AdminDateWidget)
  phone = forms.CharField(required=True, max_length=100)
  date_picked = forms.DateField(widget = widgets.AdminDateWidget)
  date_paid = forms.DateField(widget = widgets.AdminDateWidget)
  date_shipped = forms.DateField(widget = widgets.AdminDateWidget)
  tracking_number = forms.CharField(label='Tracking Number', required=True, max_length=100)
  #user (owner)

  def clean_tracking_number(self):
    tracking_count = hmod.Order.objects.filter(tracking_number=self.cleaned_data['tracking_number']).exclude(id=self.oderid).count() #self aka (this) calls form.oderid because this section of the area is IN the form
    if tracking_count >= 1:
      raise forms.ValidationError("It seems we already have a oder entered under this tracking number.  Please verify and try again.")
    return self.cleaned_data['tracking_number']

######################################################
###  Creates a new oder
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def create(request):
  # params = {}

  order = hmod.Order()
  order.order_date = None
  order.phone = ''
  order.date_picked = None
  order.date_paid = None
  order.date_shipped = None
  order.tracking_number = ''
  order.save()

  return HttpResponseRedirect('/inventory/order.edit/{}'.format(order.id))

######################################################
###  Deletes a new oder
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def delete(request):
  try:
    oder = hmod.Order.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/inventory/order/')
  order.delete()
  return HttpResponseRedirect('/inventory/order/')