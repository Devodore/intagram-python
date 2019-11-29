from django.shortcuts import render
from django.http import HttpResponse
from photos.models import Photo
from django.views.generic.edit import CreateView

# Create your views here.

def photo_index(request):
    photos = Photo.objects.all()
    return render(request, "photos/list_photos.html", {"photo_list": photos})

class PhotoCreateView(CreateView):
    model = Photo
    fields = ["title", "photo_image"]
    template_name = "photos/photo_form.html"