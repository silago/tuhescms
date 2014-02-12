# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django_thumbs.db.models import ImageWithThumbsField
from autoslug.fields import AutoSlugField
#для миграций превьюшек
from django.forms import ModelForm

class Slider(models.Model):
        image		=       ImageWithThumbsField(upload_to='slides', sizes=((125,125),(300,300)), blank=True, verbose_name=u"Фото")
        title           =       models.CharField(max_length=255, verbose_name=u"Заголовок")
        #alias           =       AutoSlugField(populate_from=title)
        text            =       models.TextField(max_length=255,verbose_name=u"Текст")
        def __unicode__(self):
                return self.title
        class Meta:
                verbose_name = " Слайдр "
                verbose_name_plural = " Слайды "



# Create your models here.
