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
from django.contrib.auth import authenticate, login
from .. import dmp_render, dmp_render_to_response
from django.contrib.auth.decorators import login_required
import requests
import datetime

templater = get_renderer('inventory')

@view_function
def process_request(request):
  params = {}

  total_price = 0
  shopping_cart0 = request.session['shopping_cart0']
  shopping_cart1 = request.session['shopping_cart1']

  for item in shopping_cart0:
    qty = shopping_cart0.get(item)
    product = hmod.Product.objects.get(id=item)
    total_price += product.current_price * qty

  for item in shopping_cart1:
    qty = shopping_cart1.get(item)
    product = hmod.Item.objects.get(id=item)
    total_price += product.standard_rental_price * qty

  if request.user.is_authenticated():
    user = request.user

  form = CheckoutForm(initial={
    'total_cost': total_price,
    'first_name': user.first_name,
    'last_name': user.last_name,
  })
  if request.method == 'POST':
    form = CheckoutForm(request.POST)
    if form.is_valid():
      for item in shopping_cart1:
        product = hmod.Item.objects.get(id=item)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(product.name)
        # product1 = hmod.Item.objects.get(id=product)
        now = datetime.datetime.now()
        
        user = request.user
        userid = user.id
        userGuid = hmod.User.objects.get(id=userid)
        rental = hmod.Rental()
        rental.userid = userGuid
        rental.itemid = product
        rental.rental_time = now
        rental.due_date = now + datetime.timedelta(days=1, hours=3)
        rental.save()
      print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
      # print(rental.userid)

    return HttpResponseRedirect('/inventory/shoppingcart.receipt/')

  pid = request.urlparams[0]
  qty = request.urlparams[1]
  params['form'] = form
  params['shopping_cart0'] = request.session['shopping_cart0']
  params['shopping_cart1'] = request.session['shopping_cart1']
  request.session.modified = True
  return templater.render_to_response(request, 'checkout.html', params)

class CheckoutForm(forms.Form):
  first_name = forms.CharField(label='First Name')
  last_name = forms.CharField(label='Last Name')
  card_type = forms.CharField(label='Card Type')
  card_number = forms.CharField(label='Card Number')
  exp_month = forms.CharField(label='Expiration Month')
  exp_year = forms.CharField(label='Expiration Year')
  cvc = forms.CharField(label='CVC')
  total_cost = forms.CharField(label='Total Cost')

  def clean_card(self):
    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = 'f45d3ef2b3438ed3066ba00442f9828f'
    name = self.cleaned_data['first_name' + ' ' + 'last_name']
    r = requests.post(API_URL, data={
      'apiKey': API_KEY,
      'currency': 'usd',
      'amount': self.cleaned_data['total_cost'],
      'type': self.cleaned_data['card_type'],
      'number': self.cleaned_data['card_number'],
      'exp_month': self.cleaned_data['exp_month'],
      'exp_year': self.cleaned_data['exp_year'],
      'cvc': self.cleaned_data['cvc'],
      'name': name,
      'description': 'Charge for CHF',
      })

    print(r.text)

    resp = r.json()
    if 'error' in resp:
        print('ERROR: ', resp['error'])
    else:
      print(resp.keys())
      print(resp['ID'])

    params = {}
    # pid = request.urlparams[0]
    # qty = request.urlparams[1]

    # params['shopping_cart0'] = request.session['shopping_cart0']
    # params['shopping_cart1'] = request.session['shopping_cart1']
    #######delete the cart?#######
    # del request.session['shopping_cart']
    return templater.render_to_response(request, 'shoppingcart.receipt.html', params)