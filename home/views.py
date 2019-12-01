from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

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
    if request.method == 'POST':
        first_name = request.POST.get(
            'first_name'
        , '')
        last_name = request.POST.get(
            'last_name'
        , '')
        email = request.POST.get(
            'email'
        , '')
        phone = request.POST.get(
            'phone'
        , '')

        message = request.POST.get('message', '')
        template = get_template('contact_template.txt')
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone':phone,
            'message': message,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Evergreen Tradesource",
            ['karthikdotnet@gmail.com'],
            headers = {'Reply-To': email }
        )
        email.send()
        return redirect('contact_us')
    return render(request, 'contact_us.html', {})
