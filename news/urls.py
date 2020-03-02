from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings    

urlpatterns = [
    path('',views.all_photos, name = 'home'),
    path('search_results/', views.search_results, name = 'search_results'),
    path('image/<image_id>/',views.single_image,name ='image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)