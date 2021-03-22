from django.urls import path
from .views import indexPageView, homePageView, logout


urlpatterns = [
    path("", indexPageView, name="index"), 
    path("home", homePageView, name="home"), 
    path("logout", logout, name="logout")
]

