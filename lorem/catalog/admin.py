from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from catalog.models import *

class AdvertismentAdmin(admin.ModelAdmin):
	pass

#admin.site.register(City, AdvertismentAdmin)
admin.site.register(Category, MPTTModelAdmin)
#admin.site.register(CategoryField, AdvertismentAdmin)
admin.site.register(Item, AdvertismentAdmin)
admin.site.register(CategoryField, AdvertismentAdmin)
admin.site.register(FieldValues, AdvertismentAdmin)
#admin.site.register(AdvertismentImage, AdvertismentAdmin)

#admin.site.register(AdvertismentFieldValues,AdvertismentAdmin)
#admin.sites.register(
#admin.sites.register(
#admin.sites.register(

