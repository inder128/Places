from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

def Home(request):
	return render(request, 'pages/home.html', {'places' : [1, 2, 3, 4, 5, 6, 7]})

def NewPlace(request):
	if(request.user.is_authenticated):
		return HttpResponse("new place")
	else:
		messages.error(request, "Please login first!!!")
		return redirect('/login')