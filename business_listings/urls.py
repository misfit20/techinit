from django.urls import path

from . import views

app_name = "business_listings"

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:Business_id>", views.Bus, name="busp"),
    path('submit_review/<int:business_id>/', views.submit_review, name='submit_review'),

]