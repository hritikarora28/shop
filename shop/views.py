from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    #products = Product.objects.all()
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    #allProds = [[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    allProds =[]
    catprod = Product.objects.values('product_catergory', 'id')
    cats = {item['product_catergory'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(product_catergory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, len(prod)), nSlides])
    params = {'allProds':allProds }

    return render(request,"shop/index.html", params)

def About(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def Tracker(request):
    return HttpResponse("We are at tracker")

def Search(request):
    return HttpResponse("We are at search")

def ProductView(request):
    return HttpResponse("We are at product view")

def Checkout(request):
    return HttpResponse("We are at checkout")