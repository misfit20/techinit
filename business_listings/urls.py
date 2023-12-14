from django.urls import path

from . import views

app_name = "business_listings"

urlpatterns = [
    path("", views.index, name = "index")

]