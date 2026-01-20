from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
#
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', views.home, name='home'),
#    #path('', views.home, name='home'),
#    #path('menu/', views.menu, name='menu'),
#    path('booking/', views.booking, name='booking'),
#    #path('reviews/', views.reviews, name='reviews'),
#]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)