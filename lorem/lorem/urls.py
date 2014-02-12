from django.conf.urls import patterns, include, url

#from userstats.signals import *

import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from catalog import views as adv
from tuhes_basket import views as basket
from pages import views as pgs
#from userstats import views as us
from filebrowser.sites import site
from feedback.views import feedback
admin.autodiscover()

from menuz import registry
registry.autodiscover()




urlpatterns = patterns('',
	
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'', include('menuz.urls')),
    url (r'^basket/',basket.view),    
    url (r'^feedback/',feedback),

    #url(r'^accounts/register/', us.registration),
    
    # Examples:
    # url(r'^$', 'lorem.views.home', name='home'),
    # url(r'^lorem/', include('lorem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin 
    #documentation:
     url(r'^search/*', adv.search),
    # url(r'^Item/up/(\d*)/', adv.up),
    #url(r'^Item/delete/(\d*)/', adv.delete),
    #url(r'^warring/', us.setWarring),
    url(r'^page/(.*)/', pgs.page),
    #url(r'^profile/(.*)/', us.profile),

      
    #url(r'^Items/add', adv.add),
    url(r'^category/(.*)/', adv.category),    
    url(r'^catalog/items/(\d*)/', adv.Item),    
    #url(r'^city/(\d*)/', adv.setcity),    
    url(r'^accounts/', include('registration.backends.default.urls')),
	url('foundation', include('foundation.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/filebrowser/', include(site.urls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url('', adv.index),
)
