from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	             path("UserLogin.html", views.UserLogin, name="UserLogin"),
		     path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
		     path("ScrapeMap.html", views.ScrapeMap, name="ScrapeMap"),
		     path("ScrapeMapAction", views.ScrapeMapAction, name="ScrapeMapAction"),
		     path("Register.html", views.Register, name="Register"),
		     path("RegisterAction", views.RegisterAction, name="RegisterAction"),
		     
		      ]