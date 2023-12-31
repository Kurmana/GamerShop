from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    product = Product.objects.all()[:2]
    return render(request, 'index.html', {'product': product})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def product(request):
    product = Product.objects.all()
    return render(request, 'product.html', {'products': product})


def remot(request):
    return render(request, 'remot.html')


def video(request):
    return render(request, 'video.html')


def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})

