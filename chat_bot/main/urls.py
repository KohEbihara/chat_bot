from django.urls import path

from . import views

urlpatterns = [
    path("", views.talk_room, name="talk_room"),
]