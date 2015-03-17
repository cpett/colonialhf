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

templater = get_renderer('inventory')

######################################################
###  Shows the list of products
@view_function
def process_request(request):
  params = {}

  if 'shopping_cart' not in request.session:
    request.session['shopping_cart'] = {}


  params['shopping_cart'] = request.session['shopping_cart']

  return templater.render_to_response(request, 'shoppingcart.html', params)

@view_function
def add(request):
  params = {}

  pid = request.urlparams[0]
  qty = request.urlparams[1]

  if 'shopping_cart' not in request.session:
    request.session['shopping_cart'] = {}

  if pid not in request.session['shopping_cart']:
    request.session['shopping_cart'][ pid ] = int(qty)
  else:
    request.session['shopping_cart'][ pid ] += int(qty)

  params['shopping_cart'] = request.session['shopping_cart']
  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.html', params)

@view_function
def review(request):
  params = {}

  pid = request.urlparams[0]
  qty = request.urlparams[1]

  params['shopping_cart'] = request.session['shopping_cart']
  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.review.html', params)

@view_function
def remove(request):
  params = {}

  del request.session['shopping_cart'][request.urlparams[0]]

  params['shopping_cart'] = request.session['shopping_cart']
  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.remove.html', params)

@view_function
def removeitem(request):
  params = {}

  del request.session['shopping_cart'][request.urlparams[0]]

  params['shopping_cart'] = request.session['shopping_cart']
  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.html', params)

@view_function
@login_required(login_url='/homepage/index/')
def checkout(request):
  params = {}

  # try:
  #   order = hmod.Order.objects.get(id=request.urlparams[0])
  # except hmod.Order.DoesNotExist:
  #   return HttpResponseRedirect('/inventory/order/')

  form = CheckoutForm()
  #   initial={
  #   'first_name': 
  #   'last_name': 
  #   'credit_card': 
  #   'card_numberar': order.date_paid,
  # })
  # if request.method == 'POST':
  #   form = CheckoutForm(request.POST)
  #   form.oderid = order.id
  #   if form.is_valid():
  #     order.date_paid = form.cleaned_data['date_paid']
  #     order.date_shipped = form.cleaned_data['date_shipped']
  #     order.tracking_number = form.cleaned_data['tracking_number']
  #     order.save()
  #     return HttpResponseRedirect('/inventory/order/')      


  params['form'] = form
  # params['order'] = order

  pid = request.urlparams[0]
  qty = request.urlparams[1]

  params['shopping_cart'] = request.session['shopping_cart']
  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.checkout.html', params)

class CheckoutForm(forms.Form):
  first_name = forms.CharField(label='First Name')
  last_name = forms.CharField(label='Last Name')
  address = forms.CharField()
  city = forms.CharField()
  state = forms.CharField()
  zip = forms.CharField()
  phone = forms.CharField()
  credit_card = forms.CharField(label='Credit Card')
  card_number = forms.CharField(label='Card Number')
  expiration_date = forms.CharField(label='Expiration Date')

  # def clean_tracking_number(self):
  #   tracking_count = hmod.Order.objects.filter(tracking_number=self.cleaned_data['tracking_number']).exclude(id=self.oderid).count() #self aka (this) calls form.oderid because this section of the area is IN the form
  #   if tracking_count >= 1:
  #     raise forms.ValidationError("It seems we already have a oder entered under this tracking number.  Please verify and try again.")
  #   return self.cleaned_data['tracking_number']

@view_function
def receipt(request):
  params = {}

  pid = request.urlparams[0]
  qty = request.urlparams[1]

  params['shopping_cart'] = request.session['shopping_cart']
  request.session.modified = True

  #######delete the cart?#######
  del request.session['shopping_cart']

  return templater.render_to_response(request, 'shoppingcart.receipt.html', params)

@view_function
def loginform(request):
  template_vars = {}

  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      login(request, user)
      return HttpResponse('''
        <script>
          window.location.href = "/inventory/shoppingcart.checkout/"
        </script>
        ''')

  template_vars['form'] = form

  return dmp_render_to_response(request, 'shoppingcart.loginform.html', template_vars)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  def clean(self):
    user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
    if user == None:
      raise forms.ValidationError('Something went wrong.  Please try again.')
    return self.cleaned_data