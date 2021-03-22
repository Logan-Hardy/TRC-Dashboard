from django.urls import path
from .views import trcDetailsPageView, TrcDetailsPageView, trcMeetingsPageView, summaryPageView, viewMissionariesPageView

urlpatterns = [
    path("", trcDetailsPageView, name="trcDetails"),
    path("TrcDetails/<int:missionary_id>", TrcDetailsPageView, name="TrcDetails"),
    path("summary/", summaryPageView, name="summary"),
    path("meetings/", trcMeetingsPageView, name="trcMeetings"),
    path("missionaries/", viewMissionariesPageView, name="missionaries")
]
