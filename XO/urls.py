from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("game/<int:num>", views.game, name="game"),
    path("win", views.win, name="win"),
]
