# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django_thumbs.db.models import ImageWithThumbsField
from autoslug.fields import AutoSlugField
#для миграций превьюшек
from south.modelsinspector import add_introspection_rules
from django.forms import ModelForm
#from myadpp.models import Article
from mptt.models import MPTTModel, TreeForeignKey
from django.core.urlresolvers import reverse


#from lib.thumbs import ImageWithThumbsField
if 1:
    add_introspection_rules([
        (
            [ImageWithThumbsField], # Class(es) these apply to
            [],         # Positional arguments (not used)
            {           # Keyword argument
                "sizes": ["sizes", {}],
            },
        ),
    ], ["^django_thumbs\.db\.models\.ImageWithThumbsField"])




class Category(MPTTModel):
	parent          =       TreeForeignKey('self', null=True, blank=True, verbose_name='Родительский элемент')
	name			=	models.CharField(max_length=255,verbose_name=u"Название")
	alias			=	AutoSlugField(populate_from='name', unique=True,verbose_name=u"Псевдоним")
	position        =       models.IntegerField(null=True, blank=True, verbose_name='Позиция')
	meta_description=       models.TextField(max_length=255,verbose_name="meta_description", null=True, blank=True)
	meta_keywords   =       models.TextField(max_length=255,verbose_name="meta_keywords", null=True, blank=True)

        def save(self, *args, **kwargs):
                if not self.position:

					p = Category.objects.order_by('-position')[:1]
					#print(p)
					if (p):
							self.position = p[0].position+1
					else: self.position = 0
                super(Category, self).save(*args, **kwargs)

        class MPTTMeta:
                order_insertion_by = ['position']

	#@models.permalink
	def get_absolute_url(self):
		return reverse('catalog.views.category', args=(str(self.alias),))
        
	def __unicode__(self):
		return self.name	
	class Meta:
		verbose_name = " Категория"
		verbose_name_plural = " Категории"

class CategoryField(models.Model):
	name		=	models.CharField(max_length=255,verbose_name=u"Имя")
	category	=	models.ManyToManyField(Category,verbose_name=u"Категория")
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = " Поле категорий "
		verbose_name_plural = " Поля категорий "

class Item(models.Model):
	#parent          =       models.ForeignKey('self', null=True, blank=True, verbose_name='Родительский элемент')
	#owner	 	= 	models.ForeignKey(User, verbose_name=u"Владелец")
	#city		=	models.ForeignKey(City, verbose_name=u"Город")
	category	=	models.ForeignKey(Category,  verbose_name=u"Категория" )
	mainPhoto	=	ImageWithThumbsField(upload_to='images', sizes=((125,125),(300,300)), blank=True, verbose_name=u"Фото")
	title		=	models.CharField(max_length=255, verbose_name=u"Заголовок")
	alias		=	AutoSlugField(populate_from='title')
	text		=	models.TextField(max_length=255,verbose_name=u"Текст")
	#price		=	models.CharField(max_length=255,blank = True, verbose_name=u"Вознаграждение")
	#typeof		=	models.CharField(max_length=255, choices = (('have','У меня есть'),('need','Я ищу')), verbose_name=u"Тип")
	date		=	models.DateTimeField(auto_now_add = True, verbose_name=u"Дата")
	#rate		=	models.IntegerField(blank=True, default=5, verbose_name=u"Рейтинг")
	#status		=	models.IntegerField(choices = ((-1,'Неактивно'),(0,'Не оплачено'),(1,'Оплачено')), default=0, verbose_name=u"Статус")
        meta_description=       models.TextField(max_length=255,verbose_name="meta_description", null=True, blank=True)
        #meta_keywords   =       models.TextField(max_length=255,verbose_name="meta_keywords")

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = " Объявление "
		verbose_name_plural = " Объявления "
    

#class AdvertismentImage(models.Model):
#	adv			=	models.ForeignKey(Advertisment,)
#	image		=	ImageWithThumbsField(upload_to='images', sizes=((125,125),(300,300)))	
#	class Meta:
#		verbose_name = " Изображение "
#		verbose_name_plural = " Изображения "

class FieldValues(models.Model):
	adv			=	models.ForeignKey(Item,verbose_name=u"Объявление")
	field		=	models.ForeignKey(CategoryField,verbose_name=u"Поле")
	value		=	models.CharField(max_length=255,verbose_name=u"Значение")
	def __unicode__(self):
		return unicode(self.adv.title+" . "+self.field.name+' . '+self.value)
	class Meta:
		verbose_name = " Дополнительный параметр объявления "
		verbose_name_plural = " Дополнительные параметры объявдения "

class AdvertismentForm(ModelForm):
	class Meta:
		model	=	Item
		fields	=	['category','mainPhoto','title','text']
	
	#	return inst
