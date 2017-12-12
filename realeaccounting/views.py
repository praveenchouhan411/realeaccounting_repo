# -*- coding: utf-8 -*-
#predefined code
from __future__ import unicode_literals
from django.shortcuts import render

#Packages required for view
from django.http import HttpResponse

#login functionality
import smtplib  

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate

from django.template.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token
#from custom_user.models import CustomUserManager as User
#from custom_user.forms import CustomUserCreationForm
from forms import MyRegistrationForm 
#from django.contrib.formtools.wizard.views import SessionWizardView
#from formtools.wizard.views import WizardView
from formtools.wizard.views import SessionWizardView

from django.core.mail import send_mail

#Class Base Template
from django.template.loader import get_template
#from django.template import Context
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView

from django.views.generic.base import TemplateView
from django.core.mail import send_mail, BadHeaderError
#from models import EmailForm


import logging
logr = logging.getLogger(__name__)
import socket
from smtplib import SMTPException


"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_HOST_USER = 'praveensinghc0@gmail.com'
EMAIL_HOST_PASSWORD = 'Pr@veen1004'
EMAIL_USE_TLS = True
"""

	

#import logging 
#logr = logging.getLogger(__name__)


# Create your views here.

def firstuser(request):
	user = "PaHu"
	html = "<html><body>Hi %s this seems to have worked safari project!</body></html>" % user
	return HttpResponse(html)
	#return render(request, "home.html")

def reale_homepage(request):
	return render(request, "home.html")


"""def index(request):
	return render(request, "index.html")
"""

def index1(request):
	return render(request, "about-us.html")

def index2(request):
	return render(request, "services.html")

def index5(request):
	return render(request, "contact-us.html")

class HelloTemplate(TemplateView):
	
	template_name = "class_template.html"
	
	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name']= 'PSK'

		return context

#Contact US View

class ContactWizard(SessionWizardView):
	template_name = "contact_form.html"

	def done(self, form_list, **kwargs):
		form_data = process_form_data(form_list)

		return render_to_response('done.html', {'form_data': form_data})


def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]
	
	logr.debug(form_data[0]['subject'])
	logr.debug(form_data[1]['sender'])
	logr.debug(form_data[2]['message'])

	send_mail(form_data[0]['subject'], from_data[2]['message'], form_data[1]['sender'], ['praveensinghc0@gmail.com'], fail_silently=True)
	
	return form_data


def test(request):
	test = "PaHuuuuuuu"
	html = "<html><body>Test Username is %s </body></html>" % test
	return HttpResponse(html)

def test_temp(request):
	#template_name = "contact_form"
	test = "This is view base template"
	return render(request, 'class_template.html')
	

"""
def process_form_data(form_list):
	
	form_data = [form.cleaned_data for form in form_list]

	#print form_data
	server = smtplib.SMTP('mail.gmx.com')

	logr.debug(form_data[0]['subject'])
	logr.debug(form_data[1]['sender'])
	logr.debug(form_data[2]['message'])
	
	#to_email = [form_data[1]['sender'], 'praveensinghc0@gmail.com'] 

	#send_mail(subject, contact_message, from_email, [to_email], fail_silently = True )

	send_mail(form_data[0]['subject'], form_data[2]['message'], form_data[1]['sender'],
			['praveensinghc0@gmail.com'], fail_silently= True )		

	return form_data

def sendmail(request):
      if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
          firstname = form.cleaned_data['firstname']
          lastname = form.cleaned_data['lastname']
          email = form.cleaned_data['email']
          subject = form.cleaned_data['subject']
          botcheck = form.cleaned_data['botcheck'].lower()
          message = form.cleaned_data['message']
          if botcheck == 'yes':
            try:
              fullemail = firstname + " " + lastname + " " + "<" + email + ">"
              send_mail(subject, message, fullemail, ['SENDTOUSER@DOMAIN.COM'])
              return HttpResponseRedirect('/email/thankyou/')
            except:
              return HttpResponseRedirect('/email/')
        else:
          return HttpResponseRedirect('/email/')
      else:
        return HttpResponseRedirect('/email/') 
"""
   
