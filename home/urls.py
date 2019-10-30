from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('Services/', views.services, name = 'services'),
    path('Products/', views.products, name = 'products'),
    path('About Us/', views.about_us, name = 'about_us'),
    path('Contact Us/', views.contact_us, name = 'contact_us')
]
