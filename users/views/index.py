from django.conf import settings
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from datetime import datetime
from django import forms
from .. import dmp_render, dmp_render_to_response
import homepage.models as hmod
from django.views.decorators.csrf import csrf_exempt
from homepage.State import State
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType
from django.contrib.auth import authenticate, login
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO

@view_function
def process_request(request):
  template_vars = {}

  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      login(request, user)
      #return HttpResponseRedirect('/homepage/index/')

  template_vars['form'] = form

  return dmp_render_to_response(request, 'index.html', template_vars)

@view_function
def loginform(request):
  template_vars = {}

  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      s = Server('www.thecolonialheritage.com', port=8889, get_info=GET_ALL_INFO)
      print('connected')
      c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='cody@thecolonialheritage.local', password='Password1', authentication=AUTH_SIMPLE)
      print("connection established")
      print("end of method reached")

      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      login(request, user)
      return HttpResponse('''
        <script>
          window.location.href = window.location.href;
        </script>
        ''')

  template_vars['form'] = form

  return dmp_render_to_response(request, 'index.loginform.html', template_vars)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  def clean(self):
    user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
    if user == None:
      raise forms.ValidationError('Something went wrong.  Please try again.')
    return self.cleaned_data
