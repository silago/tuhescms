from django.contrib import admin
from pages.models import *

class PageAdmin(admin.ModelAdmin):
	pass
	class Media:
		js = [
		'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
		'/static/grappelli/tinymce_setup/tinymce_setup.js',
		]

admin.site.register(Page, PageAdmin)


#admin.sites.register(
#admin.sites.register(
#admin.sites.register(

