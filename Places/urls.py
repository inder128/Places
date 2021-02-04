from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("App.urls")),
    path('register', views.Register),
    path('login', views.Login),
    path('logout', views.Logout),
    path('accounts/', include('allauth.urls')),
]