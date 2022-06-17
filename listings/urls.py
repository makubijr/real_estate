from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.listing_listings, name=('listings')),
    path('create/', views.listing_create, name=('create')),
    path('update/<id>/', views.listing_update, name=('update')),
    path('delete/<id>/', views.listing_delete, name=('delete')),
    path('listing/<id>/', views.listing_listing, name=('listings')),
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)