from django.contrib import admin
from slider.models import *

class SliderAdmin(admin.ModelAdmin):
	pass

admin.site.register(Slider, SliderAdmin)


#admin.sites.register(
#admin.sites.register(
#admin.sites.register(

