from django import forms, http
from django.shortcuts import render
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView

from reviews import models
# Create your views here.


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request,"reviews/review.html",{
#                 "form":form,
#             })
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save() # because of model form
#             print(form.cleaned_data)
#             return HttpResponseRedirect("/thank-you-url")
#         else:
#             form  = ReviewForm()
#         return render(request,"reviews/review.html",{
#                 "form":form,
#             })


class ReviewView(CreateView):
    form_class = ReviewForm
    model = Review
    template_name = "reviews/review.html"
    success_url = "/thank-you-url"
    # fields = '__all__'
    

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you-url"
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ThankYouView(View):
#     def get(self, request):
#          return render(request,"reviews/thank_you.html")


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = " to pass a value into template"
        return context
    






# def review(request):
#     # if request.method == "POST":
#     #     result = request.POST
#     #     entered_username = result.get('username')
#     #     print(entered_username)
#     #     if entered_username =="":
#     #         return render(request,"reviews/review.html",{
#     #             "has_error":True,
#     #         })
#     #     return HttpResponseRedirect("/thank-you-url")
#     # return render(request,"reviews/review.html",{
#     #             "has_error":False,
#     #         })
#     form = None
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review_obj = Review(user_name = form.cleaned_data['user_name'],
#             # review_text = form.cleaned_data['review_text'],
#             # rating = form.cleaned_data['rating'])
#             # review_obj.save()
#             form.save() # because of model form
#             print(form.cleaned_data)

#             return HttpResponseRedirect("/thank-you-url")
#         else:
#             form  = ReviewForm()
#     return render(request,"reviews/review.html",{
#                 "form":form,
#             })



# def thank_you(request):
#     return render(request,"reviews/thank_you.html")


# class ReviewListView(TemplateView):
#     template_name = "reviews/reviews_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["reviews"] = Review.objects.all()
#         return context

class ReviewListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "my_reviews" # other wise it'll name as object_list on the template
    def get_queryset(self):
        result = super().get_queryset()
        return result.filter(rating__gt=4)
    


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         id = kwargs.get('id')
#         context["review"] = Review.objects.get(pk=id)
#         return context
    

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = self.request.session.get("favourite_review")
        loaded_review = self.object
        print(loaded_review.id)
        print(review_id)
        print((str(loaded_review.id) == str(review_id)))
        context["is_favourite"] = (str(loaded_review.id) == str(review_id))
        return context
    


class AddFavouriteView(View):

    def post(self, request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        print(review_id)
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/"+review_id)
        
