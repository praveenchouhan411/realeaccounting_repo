"""realeaccounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib.auth.views import login
from registration.backends.hmac import urls
from django.conf.urls import url, include
from django.contrib import admin
import realeaccounting.views 
from realeaccounting.views import HelloTemplate
#from contact_form import urls
admin.autodiscover()

#Contact US Packages
from realeaccounting.forms import ContactForm1, ContactForm2, ContactForm3
from realeaccounting.views import ContactWizard

#Email Functionality
from django.conf import settings
from django.views.generic.base import TemplateView
from views import *
import registration

urlpatterns = [
    
    url(r'^accounts/', include(registration.backends.hmac.urls)),   
    url(r'^accounts/profile/$', realeaccounting.views.reale_homepage),
    #url(r'^contact-form/', include('contact_form.urls')),
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', realeaccounting.views.reale_homepage),
    url(r'^about-us/$', realeaccounting.views.index1),
    url(r'^contact-us/$', realeaccounting.views.index5),
    url(r'^services/$', realeaccounting.views.index2),
    url(r'^test/$', realeaccounting.views.test),
    #url(r'^contact/$', ContactWizard.as_view(), name ='ContactWizard'),
    url(r'^class_temp/$', HelloTemplate.as_view(), name='HelloTemplate'),   
    #url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
    url(r'^test_temp/$', realeaccounting.views.test_temp),
    
 
]
