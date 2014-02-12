# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django_thumbs.db.models import ImageWithThumbsField
from autoslug.fields import AutoSlugField
#для миграций превьюшек
from django.forms import ModelForm
from mptt.models import MPTTModel, TreeForeignKey
import os,sys
pageTemplateFolder = 'pages/'
from django.conf import settings
from django.core.urlresolvers import reverse





class Page(MPTTModel):
	parent	 	= 	TreeForeignKey('self', null=True, blank=True, verbose_name='Родительский элемент')
	title		=	models.CharField(max_length=255, verbose_name="Заголовк")
	alias		=	AutoSlugField(populate_from='title', unique=True)
	text		=	models.TextField(max_length=255,verbose_name="Текст")
	date		=	models.DateTimeField(auto_now_add = True)
	position	=	models.IntegerField(null=True, blank=True, verbose_name='Позиция')	
	template	=	models.CharField(max_length=255, choices=((pageTemplateFolder+f,f) for f in [f for f in os.listdir(settings.TEMPLATE_DIRS[0]+pageTemplateFolder)])) 
	meta_description=	models.TextField(max_length=255,verbose_name="meta_description", null=True, blank=True)
	meta_keywords	=	models.TextField(max_length=255,verbose_name="meta_keywords")
		
	def get_absolute_url(self):
		return reverse('pages.views.page', args=(str(self.alias),))
		
	class MPTTMeta:
		order_insertion_by = ['position']
	
	def save(self, *args, **kwargs):
		if not self.position:
			p = Page.objects.all().order_by('-position')[:1]
			#print p[0].position
			#print "___"
			if (p.count()>0):
				self.position = p[0].position+1
			else: self.position = 0
		super(Page, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = " Страница "
		verbose_name_plural = " Страницы "
    
