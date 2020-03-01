from django.shortcuts import render , redirect
from .models import Image,Category,Location

# Create your views here.
def home(request):
    
    return render(request, 'all-images/index.html')
    print('hello world')

def search_results(request):
        if 'category' in request.GET and request.GET["category"]:
            search_term = request.GET.get("category")
            searched_category = Category.search_category(search_term)
            message = f"{search_term}"

            searched_image = Image.get_pics_cat(searched_category)

            return redirect(request, 'all-images/search.html',{"message":message,'photo':searched_image, 'locations':locations})

        else:
            message = 'You haven\'t searched for any item'
            return render(request, 'all-images/search.html', {'message':message})