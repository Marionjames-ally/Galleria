from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings    

urlpatterns = [
    path('',views.home, name = 'home'),
    path('search/', views.search_results, name = 'search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)