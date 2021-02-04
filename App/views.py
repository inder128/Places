from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Place, Comment, Image
from .forms import PlaceForm
import requests


def Home(request):
	return render(request, 'pages/home.html', {'places' : [1, 2, 3, 4, 5, 6, 7]})

def NewPlace(request):
	if(request.user.is_authenticated):
		return render(request, 'pages/placeForm.html', {'form': PlaceForm()})
	else:
		messages.error(request, "Please login first!!!")
		return redirect('/login')

def Place(request):
	# post a place
	if request.method == "POST":
		form = PlaceForm(request.POST, request.FILES)
		imagesList = request.FILES.getlist('images')
		if form.is_valid():
			place = form.save(commit=False)
			place.images = None
			place.author = request.user
			gadd = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + "+".join(place.address.split()) + '&key=AIzaSyBiAJZoPr2LmHh9CRquaUYqIaZuvx4IxIE')
			place.googleAddress = gadd.json()['results'][0]['formatted_address']
			place.lat = gadd.json()['results'][0]['geometry']['location']['lat']
			place.lng = gadd.json()['results'][0]['geometry']['location']['lng']
			place.save()
			for image in imagesList:
				Image(place = place, image = image).save()
			messages.success(request, "Successfuly added Place!!!")
		return redirect('/')