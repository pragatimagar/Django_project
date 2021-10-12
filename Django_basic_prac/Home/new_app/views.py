from django.shortcuts import render,HttpResponse
from datetime import datetime
from new_app.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable1': 'this is sent',
        'variable2': 'value sent'
    }
    return render(request, 'index.html',context)
    

def brands(request):
    return render(request, 'brands.html')
      

def categories(request):
    return render(request, 'categories.html')
           

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        contact=Contact(name=name, email=email, phone=phone, address=address, date=datetime.today())
        contact.save()
        messages.success(request, 'Your details has been sent!')

    return render(request, 'contact.html')
           