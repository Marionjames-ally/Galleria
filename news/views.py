from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def home(request):
    
    return render(request, 'all-images/index.html')
    print('hello world')



def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-Images/search.html',{"message":message,"articles": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})