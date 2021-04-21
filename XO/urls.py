from django.urls import path
from . import views

urlpatterns = [
    path("<int:num>", views.index, name="index")
]
