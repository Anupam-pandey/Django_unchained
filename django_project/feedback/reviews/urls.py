from django.urls import path
from . import views
urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you-url', views.ThankYouView.as_view()),
    path('reviews', views.ReviewListView.as_view()),
    path('reviews/favourite', views.AddFavouriteView.as_view()),
    path('reviews/<int:pk>', views.SingleReviewView.as_view()),
    #  path('posts',views.posts, name="posts-page" ),
]