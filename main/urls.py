from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('menu/', views.menu, name='menu'),
    path('reviews/', views.reviews, name='reviews'),
]   