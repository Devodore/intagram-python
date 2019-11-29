from django.shortcuts import render
from django.http import HttpResponse
from photos.models import Photo

# Create your views here.

def photo_index(request):
    photos = Photo.objects.all()
    return render(request, "photos/list_photos.html", {"photo_list": photos})
