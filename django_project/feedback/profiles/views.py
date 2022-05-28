from django import http
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.



# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)



class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
    fields = "__all__"


class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST,request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(user_image=request.FILES['user_image'])
#             profile.save()
#             # image = request.FILES['image']
#             # image = request.FILES['user_image']
#             # print(image)
#             # store_file(image)
#             return HttpResponseRedirect("/profiles")
#         return HttpResponseRedirect("/profiles",{
#             "form": submitted_form
#         })