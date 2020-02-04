from django.shortcuts import render
from .models import Location, Category, Photo

# Create your views here.
def welcome(request):
    return render (request,'base.html')
def category(request):
    return render (request,'categories.html')
def photos(request):
    photos = Photo.objects.all()
    return render (request,'images.html', {"photos":photos})