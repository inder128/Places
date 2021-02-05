from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Place as PlaceTable, Comment, Image
from .forms import PlaceForm
import requests


def Home(request):
	# get request to home page
	return render(request, 'pages/home.html', {'places': PlaceTable.objects.all()})

def NewPlace(request, newCopy = False):
	# get request to add form page
	if request.method == "GET":
		if request.user.is_authenticated:
			return render(request, 'pages/placeForm.html', {'form': PlaceForm()})
		else:
			messages.error(request, "Please login first!!!")
			return redirect('/login')

	# to add a place
	if request.method == "POST":
		form = PlaceForm(request.POST, request.FILES)
		imagesList = request.FILES.getlist('images')
		if form.is_valid():
			place = form.save(commit=False)
			place.author = request.user
			gadd = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + "+".join(place.address.split()) + '&key=AIzaSyBiAJZoPr2LmHh9CRquaUYqIaZuvx4IxIE')
			place.googleAddress = gadd.json()['results'][0]['formatted_address']
			place.lat = gadd.json()['results'][0]['geometry']['location']['lat']
			place.lng = gadd.json()['results'][0]['geometry']['location']['lng']
			place.save()
			for image in imagesList:
				Image(place = place, image = image).save()
			if newCopy:
				return place
			messages.success(request, "Operation Successful!!!")
			return redirect('/' + str(place.id))
		else:
			messages.success(request, "Can't Add Place. Something went wrong!!!")
			return redirect('/')


def Place(request, id):
	# to get the place
	if request.method == "GET":
		place = PlaceTable.objects.filter(id = id)[0]
		images = Image.objects.filter(place = place)
		return render(request, 'pages/place.html', {'place': place, 'images':images})

	place = PlaceTable.objects.filter(id = id)[0]

	if place.author.id != request.user.id:
		messages.error(request, "You are not the auther of this Place. So, You are not allowed to do this operation!!!")
		return redirect('/' + str(id))

	# to delete this place
	if request.GET.get('method') == "DELETE":
		Image.objects.filter(place = place).delete()
		place.comments.all().delete()
		place.delete()
		messages.success(request, "Successfuly deleted Place!!!")
		return redirect('/')
		
	# to update the place
	if request.method == "POST":	
		Image.objects.filter(place = place).delete()
		newPlace = NewPlace(request, True)
		newPlace.comments.set(place.comments.all())
		place.delete()
		return redirect('/' + str(newPlace.id))


		

def EditPlace(request, id):
	place = PlaceTable.objects.filter(id=id)[0]
	if place.author.id != request.user.id:
		messages.error(request, "You are not allowed to edit this place!!!")
		return redirect('/' + str(id))
	return render(request, 'pages/editPlaceForm.html', {'place' : place,'form': PlaceForm()})

def AddComment(request, id):
	if request.user.is_authenticated:
		place = PlaceTable.objects.filter(id=id)[0]
		text = request.POST.get('text')
		author = request.user
		comment = Comment(text=text, author=author)
		comment.save()
		place.comments.add(comment)
		place.save()
		messages.success(request, "Successfuly added comment!!!")
		return redirect('/' + str(id))
	else:
		messages.error(request, "Please login first!!!")
		return redirect('/login')

def DeleteComment(request, id, cid):
	comment = Comment.objects.filter(id = cid)[0]
	if comment.author.id != request.user.id:
		messages.error(request, "You are not allowed to delete this Comment!!!")
	else:
		comment.delete()
		messages.success(request, "Successfuly deleted comment!!!")
	return redirect('/' + str(id))