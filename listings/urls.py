from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_listings, name=('listings')),
    path('listing/<id>/', views.listing_listing, name=('listings')),
    
    ]