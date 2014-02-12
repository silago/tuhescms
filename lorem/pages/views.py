from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import RequestContext
from pages.models import Page
import sys
from tuhes_breadcrumbs import t_bread

@t_bread(key="",item_model=Page)
def page(request,itemId):
	#print itemId
	#print "as"
	#print category
	item = Page.objects.get(alias=itemId)
	#itemparams = AdvertismentFieldValues.objects.filter(adv__id=itemId)
	
	return render_to_response(item.template,{'item':item,'meta_description':item.meta_description,'meta_keywords':item.meta_keywords},context_instance=RequestContext(request))
