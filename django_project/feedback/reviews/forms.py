from reviews.models import Review
from django import forms
from django.forms.forms import Form
from django.forms.widgets import Textarea
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="please enter the name")
#     rating = forms.IntegerField(label="your rating", min_value=1, max_value=5)
#     review_text = forms.CharField(label="your feedback", widget=Textarea)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['field which you dont want to mimic with the form']
        labels = {
            'user_name' : "your name here",
            'review_text' : "your review here",
            'rating' : "your rating here",
        }
        # error_messages = {
        #     'user_name':{
                
        #     }
        # }
