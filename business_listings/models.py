from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Business(models.Model):
    
    business = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.business}, {self.description}"




class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name  # Updated the __str__ method to return the customer's name
    

class Team(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    business = models.OneToOneField(Business, on_delete=models.CASCADE, related_name="team", null=True)
    
    def __str__(self):
        return f"{self.first} {self.last} - {self.position}"
    
class ReviewRating(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="review", null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, null=True)
    review = models.TextField(max_length=500, null=True)
    rating = models.FloatField()
    status = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.subject
    