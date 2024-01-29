from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating  # Assign the ReviewRating model to the form
        fields = ['subject', 'review', 'rating']