from django import forms
from django.db.models import fields
from .models import Comment

class CommentForm(forms.ModelForm):
    # user_name = forms.CharField( max_length=150)
    # user_email = forms.EmailField(max_length=454)
    # text = forms.TextField()
    # post = forms.ForeignKey(Post,on_delete=CASCADE, related_name="comments")
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {"user_name": "Your Name",
        "user_email" : "your email",
        "text": "your comment"            
        }
