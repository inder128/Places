from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("App.urls")),
    path('register', views.Register),
    path('login', views.Login),
    path('logout', views.Logout),
    path('accounts/', include('allauth.urls')),
]
