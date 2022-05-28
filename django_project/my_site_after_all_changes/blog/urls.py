from django.urls import path
from . import views
urlpatterns = [
    # path("",views.starting_page, name="starting-page" ),
    path("",views.StartingPageView.as_view(), name="starting-page" ),
    # path('posts',views.posts, name="posts-page" ),
    path('posts',views.AllPosts.as_view(), name="posts-page" ),
    # path('posts/<slug:slug>',views.post_details, name="post-details-page" ),
    path('posts/<slug:slug>',views.SinglePostView.as_view(), name="post-details-page" ),
    path('read-later',views.ReadLaterView.as_view(), name="read-later" ),
]

