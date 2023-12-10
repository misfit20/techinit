from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request, 'business_listings/index.html')



def sign_in(request):
    # Implement user sign-in logic
    pass
