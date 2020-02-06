from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('Services/', views.services, name = 'services'),
    path('Products/', views.products, name = 'products'),
    path('AboutUs/', views.about_us, name = 'about_us'),
    path('ContactUs/', views.contact_us, name = 'contact_us')
]
