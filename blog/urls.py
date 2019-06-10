from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.showvideo, name='blog-about'),
    #path('about/',views.showvideo, name='blog-about'),
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

