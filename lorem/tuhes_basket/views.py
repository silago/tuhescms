from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from catalog.models import Item
from catalog.models import Category
from django.template import RequestContext
import datetime
import re
import sys
from django.conf import settings



def objectAttrByI(obj, i):
	return True

def view(request):
	if request.session.get('basket',False):
		for i in request.session['basket'].keys():
			print i.id
			
	else:
		print "Basket is Empty"
		for item in Item.objects.all():
			print item.id
			print item.title	
						
			#print type(item)
		print "__"
		return False
	pass

#def add(request):
#	request.session['basket'].append('1')
#
#
#	pass
#
#def delete(request):
#	pass
