from django.shortcuts import render, redirect, get_object_or_404
from .models import Business, Team, ReviewRating
from .forms import ReviewForm
from django.contrib import messages
# Create your views here.


def index(request):
    businesses = Business.objects.all()
    business_reviews = get_business_reviews(businesses)
   
    return render(request, 'business_listings/index.html', {'businesses': businesses, 'business_reviews': business_reviews})


def Bus(request, Business_id):
    bus_id = Business.objects.get(pk=Business_id)
    team_objects = Team.objects.filter(business=bus_id)
    return render(request,"business_listings/busp.html", 
                  {
                      "business":bus_id,
                      "team_objects": team_objects
                       
                  })
    




def submit_review(request, business_id):
 url = request.META.get("HTTP_REFERER")   
 if request.method == "POST":
  try:
     reviews = ReviewRating.objects.get(user__id = request.user.id, business__id = business_id)
     form = ReviewForm(request.POST, instance=reviews)
     form.save()
     messages.success(request, "Review has been updated")
     return redirect(url)
  except ReviewRating.DoesNotExist:
      form = ReviewForm(request.POST)
      if form.is_valid():
          data = ReviewRating()
          data.subject = form.cleaned_data['subject']
          data.rating = form.cleaned_data['rating']
          data.review = form.cleaned_data['review']
          data.business_id = business_id
          data.user_id = request.user.id
          data.save()
          messages.success(request, "Review has been Saved")
          return redirect(url)
    
def get_business_reviews(businesses):
    business_reviews = {}
    for business in businesses:
        reviews = ReviewRating.objects.filter(business=business)
        business_reviews[business] = reviews
    return business_reviews
 
 
 
 




    