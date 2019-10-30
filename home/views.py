from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html', {})

def services(request):
   return render(request, 'services.html', {})

def products(request):
   return render(request, 'products.html', {})

def about_us(request):
   return render(request, 'about_us.html', {})

def contact_us(request):
   return render(request, 'contact_us.html', {})
