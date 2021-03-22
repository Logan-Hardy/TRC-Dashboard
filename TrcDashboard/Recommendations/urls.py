from django.urls import path
from .views import recommendationsPageView

urlpatterns = [
    path("", recommendationsPageView, name="recommendations")
]
