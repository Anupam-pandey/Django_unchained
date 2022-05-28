from django import forms
from django.forms.forms import Form




class ProfileForm(forms.Form):
    user_image = forms.FileField()