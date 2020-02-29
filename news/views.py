from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def home(request):
    return render(request, 'all-images/index.html')

def all_photos(request):
    gallery = Image.get_images()
    locations = Location.get_location()
    return render(request, 'all-images/index.html', {"gallery": gallery, "locations":locations})
