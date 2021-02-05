from django.urls import path  
from . import views 

urlpatterns = [
	path('', views.Home),	
	path('new/', views.NewPlace),
	path('<int:id>', views.Place),
	path('<int:id>/edit', views.EditPlace),
	path('<int:id>/addcomment', views.AddComment),
	path('<int:id>/deletecomment/<int:cid>', views.DeleteComment),
]