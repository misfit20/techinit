from django.urls import path

from . import views

app_name = "signup"

urlpatterns = [
    path("", views.signup, name = "signup")
    #path("log_in", views.log_in, name = "login")
]