
from django import forms 
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm 
from django.forms import ModelForm 

# reviews/forms.py
from . import models


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ( 
            'username', 
            'email', 
            'first_name', 
            'last_name' 
        ) 


class UserForm(forms.Form): 
    username = forms.CharField(label="pseudo ", max_length=150) 


class TicketForm(ModelForm): 
    class Meta: 
        model = models.Ticket 
        fields = [ 
            'title', 
            'description', 
            'image' 
        ] 


class NewReviewForm(ModelForm): 
    class Meta: 
        model = models.Review 
        fields = [ 
            'ticket', 
            'rating', 
            'headline', 
            'body' 
        ] 
        labels = { 
            'rating': 'Rating (de 0 à 5)', 
        } 
        widgets = { 
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 15}), 
        } 


class ReviewForm(ModelForm): 
    class Meta: 
        model = models.Review 
        fields = [ 
            'ticket', 
            'rating', 
            'headline', 
            'body' 
        ] 
        labels = { 
            'rating': 'Rating (de 0 à 5)', 
        } 
        widgets = { 
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 15}), 
            'ticket': forms.HiddenInput(), 
        } 

