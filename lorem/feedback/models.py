# -*- coding: utf-8 -*
from django.db import models
from django.forms import ModelForm
from django import forms


class FeedbackForm(forms.Form):
		#user = ""
		name        =       forms.CharField(label = 'Имя')
                email        =       forms.EmailField(label = 'Email')
                text        =       forms.CharField(widget=forms.Textarea, label = 'Текст сообщения')
                capcha        =       forms.CharField(label = 'Капча')

		#mail	= False
		#text	= False
		#capcha	= False

# Create your models here.
