from django.shortcuts import render
from .models import Business
# Create your views here.


def index(request):
    businesses = Business.objects.all()
    
    return render(request, 'business_listings/index.html',
                   {
                       'businesses': Business.objects.all()
                    })







