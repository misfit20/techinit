from django.contrib import admin
from .models import Business
from .models import Customer, Team, ReviewRating

# Register your models here.
admin.site.register(Business)
admin.site.register(Customer)
admin.site.register(Team)
admin.site.register(ReviewRating)