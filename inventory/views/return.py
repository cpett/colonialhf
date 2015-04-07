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
import datetime

templater = get_renderer('inventory')

######################################################
###  Shows the list of events
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def process_request(request):
  params = {}

  returns = hmod.Rental.objects.all().order_by('-renteditem_ptr_id')

  params['returns'] = returns

  return templater.render_to_response(request, 'return.html', params)


class RentedItemForm(forms.Form):
  condition = forms.CharField(label='Condition')
  new_damage = forms.CharField(label='New Damage')
  damage_fee = forms.CharField(label='Damage Fee')
  late_fee = forms.CharField(label='Late Fee')
  # damage_fee = forms.CharField(label='Damage Fee')

  def clean_name(self):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('clean method')
    rented_item = hmod.RentedItem()
    rented_item.condition = self.cleaned_data['condition'],
    rented_item.new_damage = self.cleaned_data['new_damage'],
    rented_item.damage_fee = self.cleaned_data['damage_fee'],
    rented_item.late_fee = self.cleaned_data['late_fee'],
    
    returns = hmod.Rental.objects.all().filter(id=request.urlparams[0])
    rented_item.rental = returns.id
    rented_item.save()
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(rented_item)
    return templater.render_to_response(request, 'inventory/return.review.html', params)


@view_function
def details(request):
  params = {}

  returns = hmod.Rental.objects.all().filter(id=request.urlparams[0])

  form = RentedItemForm(initial={
      # 'name': event.name,
      # 'start_date': event.start_date,
      # 'map_file_name': event.map_file_name,
    })
  if request.method == 'POST':
    form = RentedItemForm(request.POST)

    if form.is_valid():

      damage = form.cleaned_data['damage_fee']
      damage = float(damage)

      late = form.cleaned_data['late_fee']
      late = float(late)

      fees = damage + late

      rented_item = hmod.RentedItem.objects.get(id=request.urlparams[0])
      rented_item.condition = form.cleaned_data['condition'],
      rented_item.new_damage = form.cleaned_data['new_damage'],
      rented_item.damage_fee = damage #form.cleaned_data['damage_fee'],
      rented_item.late_fee = late #form.cleaned_data['late_fee'],
      ###### final_return = hmod.Return()
      rented_item.return_time = datetime.datetime.now()
      rented_item.fees_paid = fees
      
      rented_item.rental__ptr = hmod.Rental.objects.get(id=request.urlparams[0])
      print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
      print(rented_item.rental__ptr)
      # rented_item.rental = returns
      rented_item.save()



      return HttpResponseRedirect('/inventory/return.review/') 

  params['returns'] = returns

  print(returns)
  params['form'] = form
  return templater.render_to_response(request, 'return.details.html', params)

@view_function
def review(request):
  params = {}

  returned_item = hmod.RentedItem.objects.all()
  # final_return = hmod.Return.objects.all()

  rental = hmod.Rental.objects.exclude(return_time=None).order_by('-renteditem_ptr_id')

  params['returned_item'] = returned_item
  # params['final_return'] = final_return
  params['rental'] = rental
  return templater.render_to_response(request, 'return.review.html', params)