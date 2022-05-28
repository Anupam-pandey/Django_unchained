from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse
from datetime import date
from .models import Post,Author,Tag
# Create your views here.

all_posts=[
#   {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpeg",
#         "author": "Anupam",
#         "date": date.today().strftime("%d/%m/%Y"),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Anupam",
#         "date": date.today().strftime("%d/%m/%Y"),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpeg",
#         "author": "Anupam",
#         "date": date.today().strftime("%d/%m/%Y"),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }




]

def getdate(post):
    return post.get('date');




# def starting_page(request):
#     sorted_post  =  sorted(all_posts,key=getdate)
#     latest_post = sorted_post[-3:] #top 3 posts
#     return render(request,"blog/index.html", {
#         "posts":latest_post
#     })

def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html", {
        "posts":latest_post
    })

    # latest_post = sorted_post[:3]


def posts(request):
    all_posts = Post.objects.all()
    return render(request,"blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_details(request,slug):
    # identified_post = None
    # identified_post = Post.objects.all().get(slug=slug)
    identified_post = get_object_or_404(Post,slug=slug)
    # for post in all_posts:
    #     if post['slug'] == slug:
    #         identified_post = post

    return render(request,"blog/post-details.html", {
        "post" : identified_post,
        "post_tags" : identified_post.tags.all()
    })