from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#gi
def index(request):
    return HttpResponse("XO Game")
def hello(request):
    return HttpResponse("XO Game")
