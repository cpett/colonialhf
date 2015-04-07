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
from django.core.mail import send_mail

templater = get_renderer('inventory')

######################################################
###  Shows the list of products
@view_function
def process_request(request):
  params = {}

  if 'shopping_cart0' not in request.session:
    request.session['shopping_cart0'] = {}
  if 'shopping_cart1' not in request.session:
    request.session['shopping_cart1'] = {}

  params['shopping_cart0'] = request.session['shopping_cart0']
  params['shopping_cart1'] = request.session['shopping_cart1']

  request.session.modified = true

  return templater.render_to_response(request, 'shoppingcart.html', params)

@view_function
def add(request):
  params = {}

  pid = request.urlparams[0]
  qty = request.urlparams[1]
  ptype = request.urlparams[2]

  if 'shopping_cart0' not in request.session:
      request.session['shopping_cart0'] = {}
  if 'shopping_cart1' not in request.session:
      request.session['shopping_cart1'] = {}

  if ptype == '0':
    if pid not in request.session['shopping_cart0']:
      request.session['shopping_cart0'][ pid ] = int(qty)
    else:
      request.session['shopping_cart0'][ pid ] += int(qty)
  else:
    if pid not in request.session['shopping_cart1']:
      request.session['shopping_cart1'][ pid ] = int(qty)
    else:
      request.session['shopping_cart1'][ pid ] += int(qty)
  params['shopping_cart0'] = request.session['shopping_cart0']
  params['shopping_cart1'] = request.session['shopping_cart1']

  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.html', params)

@view_function
def review(request):
  params = {}

  pid = request.urlparams[0]
  qty = request.urlparams[1]
  ptype = request.urlparams[2]

  params['shopping_cart0'] = request.session['shopping_cart0']
  params['shopping_cart1'] = request.session['shopping_cart1']
  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.review.html', params)

@view_function
def remove(request):
  params = {}
  ptype = request.urlparams[1]
  print(ptype)
  if ptype == '0':
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    del request.session['shopping_cart0'][request.urlparams[0]]
  elif ptype == '1':
    del request.session['shopping_cart1'][request.urlparams[0]]
  
  params['shopping_cart0'] = request.session['shopping_cart0']
  params['shopping_cart1'] = request.session['shopping_cart1']
  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.html', params)

@view_function
def removeitem(request):
  params = {}
  ptype = request.urlparams[1]

  if ptype == '0':
    del request.session['shopping_cart0'][request.urlparams[0]]
  elif ptype == '1':
    del request.session['shopping_cart1'][request.urlparams[0]]
  
  params['shopping_cart0'] = request.session['shopping_cart0']
  params['shopping_cart1'] = request.session['shopping_cart1']
  request.session.modified = True
  return templater.render_to_response(request, 'shoppingcart.html', params)

# @view_function
# @login_required(login_url='/homepage/index/')
# def checkout(request):
#   params = {}

#   # try:
#   #   order = hmod.Order.objects.get(id=request.urlparams[0])
#   # except hmod.Order.DoesNotExist:
#   #   return HttpResponseRedirect('/inventory/order/')

#   form = CheckoutForm()
#   #   initial={
#   #   'first_name': 
#   #   'last_name': 
#   #   'credit_card': 
#   #   'card_numberar': order.date_paid,
#   # })
#   # if request.method == 'POST':
#   #   form = CheckoutForm(request.POST)
#   #   form.oderid = order.id
#   #   if form.is_valid():
#   #     order.date_paid = form.cleaned_data['date_paid']
#   #     order.date_shipped = form.cleaned_data['date_shipped']
#   #     order.tracking_number = form.cleaned_data['tracking_number']
#   #     order.save()
#   #     return HttpResponseRedirect('/inventory/order/')      


#   params['form'] = form
#   # params['order'] = order

@view_function
def receipt(request):
  params = {}

  if 'shopping_cart0' not in request.session:
    request.session['shopping_cart0'] = {}
  if 'shopping_cart1' not in request.session:
    request.session['shopping_cart1'] = {}

  if request.user.is_authenticated():
    user = request.user
  email = user.email

  params['shopping_cart0'] = request.session['shopping_cart0']
  params['shopping_cart1'] = request.session['shopping_cart1']

  emailbody = templater.render(request, 'shoppingcart.receiptemail.html', params)
  send_mail('Colonial Heritage Receipt', emailbody, 'thecolonialheritage@gmail.com', [email], html_message = emailbody, fail_silently=False)
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
          window.location.href = "/inventory/checkout/"
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

