# Create your views here.
from feedback.models import FeedbackForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from os import remove
from django.conf import settings

def feedback(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
	else:
		form = FeedbackForm()
	return render_to_response('feedback/feedback.html', {'form': form, 'capcha':capchaIMG(request) }, context_instance = RequestContext(request))



def capchaIMG(request):
	# random generator
	from random import choice
	# PIL elements, sha for hash
	import Image, ImageDraw, ImageFont, sha
	# create a 5 char random strin and sha hash it, note that there is no big i
	SALT = settings.SECRET_KEY[:20]
	imgtext = "".join([choice('QWERTYUOPASDFGHJKLZXCVBNM') for i in range(5)])
	# create hash
	imghash = sha.new(SALT+imgtext).hexdigest()
	# create an image with the string (media is the folder with static files accessed by /site_media)
	# PIL "code" - open image, add text using font, save as new
	im=Image.open(settings.MEDIA_ROOT+'bg.jpg')
	draw=ImageDraw.Draw(im)
	font=ImageFont.truetype(settings.MEDIA_ROOT+'SHERWOOD.TTF', 26)
	draw.text((10,10),imgtext, font=font, fill=(100,100,50))
	# save as a temporary image
	# I use user IP for the filename, SITE_IMAGES_DIR_PATH - system path to folder for images
	temp = settings.MEDIA_ROOT + request.META['REMOTE_ADDR'] + '.jpg'
	tempname = request.META['REMOTE_ADDR'] + '.jpg'
	im.save(temp, "JPEG")
	return {'hash': imghash, 'tempname': tempname}
