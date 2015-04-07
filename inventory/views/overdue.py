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
from django.core.mail import send_mail

templater = get_renderer('inventory')

######################################################
###  Shows the list of events
@view_function
@permission_required('homepage.change_user', login_url='/homepage/login/')
def process_request(request):
  params = {}
  now = datetime.datetime.now()
  print('>>>>>>>>>>>>>>>>>>>>>>>>')
  print(now)

  # returns = hmod.Rental.objects.all().filter(due_date__lt=now, return_time=None)

  Batch30 = hmod.Rental.objects.filter(return_time=None, due_date__lt=(now - datetime.timedelta(days=30)), due_date__gte=(now - datetime.timedelta(days=60))).order_by('-renteditem_ptr_id')

  Batch60 = hmod.Rental.objects.filter(return_time=None, due_date__lt=(now - datetime.timedelta(days=60)), due_date__gte=(now - datetime.timedelta(days=90))).order_by('-renteditem_ptr_id')
      
  Batch90 = hmod.Rental.objects.filter(return_time=None, due_date__lt=(now - datetime.timedelta(days=90))).order_by('-renteditem_ptr_id')
        
  print(Batch90)
  # params['returns'] = returns
  params['Batch30'] = Batch30
  params['Batch60'] = Batch60
  params['Batch90'] = Batch90

  return templater.render_to_response(request, 'overdue.html', params)


@view_function
# @permission_required('homepage.change_user', login_url='/homepage/login/')
def email(request):
  params = {}
  now = datetime.datetime.now()
  Batch30 = hmod.Rental.objects.filter(return_time=None, due_date__lt=(now - datetime.timedelta(days=30)), due_date__gte=(now - datetime.timedelta(days=60)))
  Batch60 = hmod.Rental.objects.filter(return_time=None, due_date__lt=(now - datetime.timedelta(days=60)), due_date__gte=(now - datetime.timedelta(days=90)))
  Batch90 = hmod.Rental.objects.filter(return_time=None, due_date__lt=(now - datetime.timedelta(days=90)))

  for person in Batch30:
    personid = person.userid_id
    user = hmod.User.objects.get(id=person.userid_id)
    email = user.email
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(email)
    emailbody = templater.render(request, 'overdue.email.html', params)
    send_mail('Colonial Heritage Overdue Reminder', emailbody, 'thecolonialheritage@gmail.com', [email], html_message = emailbody, fail_silently=False)
  
  for person in Batch60:
    personid = person.userid_id
    user = hmod.User.objects.get(id=person.userid_id)
    email = user.email
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(email)
    emailbody = templater.render(request, 'overdue.email60.html', params)
    send_mail('Colonial Heritage Overdue Reminder', emailbody, 'thecolonialheritage@gmail.com', [email], html_message = emailbody, fail_silently=False)
   
  for person in Batch90:
    personid = person.userid_id
    user = hmod.User.objects.get(id=person.userid_id)
    email = user.email
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(email)
    emailbody = templater.render(request, 'overdue.email90.html', params)
    send_mail('Colonial Heritage Overdue Reminder', emailbody, 'thecolonialheritage@gmail.com', [email], html_message = emailbody, fail_silently=False)
  
  return HttpResponseRedirect('/inventory/overdue/')

