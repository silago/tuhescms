# -*- coding: utf-8 -*-
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
#from catalog.models import CaForm
from catalog.models import Item as AdvItem
#from catalog.models import ItemFieldValues
from catalog.models import Category
#from catalog.models import CategoryField
from django.template import RequestContext
from django.db.models import Q
from django.db.models import Count
import datetime
import re
import sys
import sys
from tuhes_breadcrumbs import t_bread


def index(request):
	return render_to_response('index.html',{},context_instance=RequestContext(request))

#def setcity(request,cityId):
#	#r = request
#	response = render_to_response('refresh.html',{},context_instance=RequestContext(request))
#	response.set_cookie('cityId',cityId)	
#	
#	return response
#	#return render_to_response('index.html',{},context_instance=RequestContext(request))
	

#def add(request):
#	if request.method == 'POST':
#		post = request.POST.copy()
#		
#		form = ItemForm(post, request.FILES)
#		if form.is_valid():
#			
#			f = form.save(commit=False)
#			f.owner = request.user
#			f.save()
#			latest = Item.objects.latest('-date')
#			lId = latest.id
#			lCat = latest.category.id
#			fields = CategoryField.objects.all()
#			for i in fields:
#				print i
#				if ('additionalField'+str(i.id)) in request.POST:
#					#print 'atata'
#					newval = ItemFieldValues(adv=Item.objects.get(id=lId), field = CategoryField.objects.get(id=i.id), value  = request.POST['additionalField'+str(i.id)])
#					newval.save()
#			
#	
#	form = ItemForm()
#	additionalFields = CategoryField.objects.all()	
#
#	return render_to_response('Items/add.html',{'form':form,'additionalFields':additionalFields}, context_instance=RequestContext(request))

@t_bread(field='alias', item_model=Category, foreignKey=('alias','parent'), foreignView=True)
def category(request,category):
	
	limitStart	= 2
	offsetStart	= 0
	#print offset
	#print "_"
	#print limit]
	limit = limitStart
	offset = 0
	if (request.GET.has_key('page')):
		if (request.GET['page'] > 0):
			offsetStart = int(request.GET['page'])
			offset = int(limit*int(request.GET['page']))
	
	limit = int(limit) + int(offset)
	

	
	
	count = AdvItem.objects.filter(category__alias=category,).count()
	Items = AdvItem.objects.filter(category__alias=category,).order_by('-date')[offset:limit]
	try:	offset = int(limit*int(request.GET['page']))
	except:
			offset = 0
	print "cccc"
	return render_to_response('advertisments/index.html',{'items':Items,'offset':offsetStart,'limit':limitStart,'count':range(0,count/limitStart)},context_instance=RequestContext(request))


#ключ я получу потом
#есть ли способ не передавать модель? нет.
#есть  ли способ не передавать ключевое поле ? наверное нет. но можно не уточняя оставить дефолт
#есть ли способ не передавать внешний ключ? хмм. нужно передавать или внешний ключ или модель, но можно выставить дефолты
#а хуле я туплю. можно же брать из родительского декоратора. хихи. или нет*?
#внутренний ключ нужен
#есть ли способо не передавать вид? нет. или урл или вид. говно.

@t_bread(field='id', item_model=AdvItem, foreignKey=('alias','category'), foreignView=category)
def Item(request,itemId):
	item = AdvItem.objects.get(id=itemId)
	return render_to_response('advertisments/item.html',{'item':item,'itemparams':{}},context_instance=RequestContext(request))


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 
    
def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query & q
        if query is None:
            query = or_query
        else:
            query = query | or_query
    return query   

def search(request):
	limitStart	= 2
	offsetStart	= 0
	#print offset
	#print "_"
	#print limit]
	limit = limitStart
	offset = 0
	if (request.GET.has_key('page')):
		if (request.GET['page'] > 0):
			offsetStart = int(request.GET['page'])
			offset = int(limit*int(request.GET['page']))
	
	limit = int(limit) + int(offset)
	
			
	if request.GET.has_key('s'):
		searchString = request.GET['s']
	
	entry_query = Q(title__icontains=searchString)	|	Q(text__icontains=searchString)	
	#entry_query = entry_query | get_query(searchString, ['Itemfieldvalues__value'])
	#entry_query = entry_query 
	
	#entry_query = entry_query & Q(Itemfieldvalues__field__hidden='1')
	
	
	
	
	count = AdvItem.objects.annotate(dcoount=Count('id')).count()
	Items = AdvItem.objects.select_related().filter(entry_query).order_by('-date').annotate(dcoount=Count('id'))
	#print unicode(Items.query)
	#Items = Item.objects.select_related().filter(
	#											Q(title__icontains=searchString)	|
	#											Q(text__icontains=searchString)		|
	#											Q(Itemfieldvalues__value=searchString)	&
	#											Q(Itemfieldvalues__field__hidden='1')
	#											
	#											).order_by('-date').annotate(dcoount=Count('id'))
	
	
	
	return render_to_response('advertisments/index.html',{'count':range(0,count/limitStart),'offset':offsetStart,'limit':limitStart, 'items':Items},context_instance=RequestContext(request))
	#items = Item.objects.filter(

# Create your views here.
