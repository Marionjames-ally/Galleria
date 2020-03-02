from django.shortcuts import render , redirect
from django.http import Http404,request,HttpResponse
from .models import Image,Category,Location
from copy import deepcopy

# Create your views here.
def all_photos(request):
    gallery = Image.get_images()
    locations = Location.get_location()
    return render(request, 'all-images/index.html', {"gallery": gallery, "locations":locations})

def search_results(request):
        
        if 'category' in request.GET and request.GET["category"]:
            search_term = request.GET.get("category")
            searched_category = Category.search_category(search_term)
            message = f"{search_term}"

            searched_image = Image.get_pics_category(searched_category)
            return render (request, 'all-images/search.html',{"message":message,'Images':searched_image})

        else:
            message = 'You haven\'t searched for any item'
            return render(request, 'all-images/search.html', {'message':message})

def single_image(request, image_id):
    try:
        gallery = Image.objects.get(id = image_id)
    except:
        raise Http404()

    locations = Location.get_location()
    return render(request, 'all-images/image.html', {"gallery":gallery, 'locations':locations})

