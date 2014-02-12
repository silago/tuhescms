from django import template
register = template.Library()
from catalog.models import Category, Item
#from advertisments.models import Advertisment, AdvertismentFieldValues
#from advertisments.models import City
from pages.models import Page
from slider.models import Slider
from django.db.models import Count
from django.db.models import F

@register.inclusion_tag('tags/slider.html',takes_context = True)	
def slider(context):
	slides	= Slider.objects.all()
	return {'list':slides}

	
@register.inclusion_tag('category_list.html',takes_context = True)
def categoryList(context):
	request = context['request']
	path_arr = request.path.split('/')
	cat = 0
	#if path_arr[1]:
	#	if path_arr[1]=='category':
	#		if path_arr[2]:
	#			cat = path_arr[2]
	#else:
	
	def setChild(categories):
		for i in categories:	
			i.children = setChild(Category.objects.filter(parent_id=i.id))
		return categories
		
		
		
	categories = setChild(Category.objects.filter(parent=None))
	
	#for i in categories:	i.children = setChild(i.id)
	
	
	return {'list':categories,'url':(request.path)}




#@register.inclusion_tag('cities_list.html',takes_context = True)
#def citiesList(context):
#	#print "________"
#	#print context
#	cities = City.objects.all()
#	request = context['request']
#	if request.COOKIES.has_key('cityId'):
#		cityId = request.COOKIES['cityId']
#	else: cityId = 0
#	cityId = int(cityId)
#	return {'list':cities,'cityId':cityId}
	
	
@register.inclusion_tag('page_list.html',takes_context = True)
def pagesList(context):
	pages = Page.objects.all()
	#request = context['request']
	return {'list':pages}
	
@register.inclusion_tag('login_top.html',takes_context = True)
def loginForm(context):
	pages = Page.objects.all()
	request = context['request']
	#request = context['request']
	return {'list':pages,'request':request}

#@register.inclusion_tag('randomAdv.html',takes_context = True)
#def randomAdv(context):
#	request = context['request']
#	if request.COOKIES.has_key('cityId'):
#		cityId = request.COOKIES['cityId']
#		advs = Advertisment.objects.filter(city__id=cityId,category__onleft=1).order_by('?')[:3]
#	else:
#		advs = Advertisment.objects.values().annotate(dcount=Count('id')).filter(category__onleft=1,advertismentfieldvalues__field__category__sortleft__id=F('advertismentfieldvalues__field__id')).order_by('advertismentfieldvalues__value')[:3]
		#advs = AdvertismentFieldValues.objects.filter(field__category__onleft=1, field__category__sortleft_id=F('field__id'))
#		print advs.query
#	return {'advs':advs,'request':request}
