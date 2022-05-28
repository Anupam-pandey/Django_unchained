from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse,HttpResponseRedirect
from datetime import date
from .models import Post,Author,Tag,Comment
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import View
from .forms import CommentForm
from django.urls import reverse
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

class StartingPageView(ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]
    model = Post
    def get_queryset(self):
        data = super().get_queryset()
        data = data[:3]
        return data
    



# def starting_page(request):
#     latest_post = Post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html", {
#         "posts":latest_post
#     })

    # latest_post = sorted_post[:3]


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request,"blog/all-posts.html", {
#         "all_posts": all_posts
#     })


class AllPosts(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class SinglePostView(View):

    def is_stored_post(self,request,post_id):
        stored_posts = request.session.get('stored_posts')
        is_saved_for_later = False
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        return is_saved_for_later

    def get(self , request,slug):
        post = Post.objects.get(slug=slug)
        post_tags = post.tags.all()
        comment_form = CommentForm()

        return render(request,"blog/post-details.html",{
        "post": post,
        "post_tags": post_tags,
        "comment_form" : comment_form,
        "comments": post.comments.all().order_by("-id"),
        "saved_for_later": self.is_stored_post(request,post.id)
        })

    def post(self, request, slug):
        comment_form  = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment_form.save()
            return HttpResponseRedirect(reverse("post-details-page", args=[slug]))
        else:
            post_tags = post.tags.all()
            return render(request,"blog/post-details.html",{
                "post": post,
                "post_tags": post_tags,
            "comment_form" : comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request,post.id)

            })

        


# class SinglePostView(DetailView):
#     model = Post
#     template_name  = "blog/post-details.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_tags"] = self.object.tags.all()
#         context["comment_form"] = CommentForm()
#         return context
    


# def post_details(request,slug):
#     # identified_post = None
#     # identified_post = Post.objects.all().get(slug=slug)
#     identified_post = get_object_or_404(Post,slug=slug)
#     # for post in all_posts:
#     #     if post['slug'] == slug:
#     #         identified_post = post

#     return render(request,"blog/post-details.html", {
#         "post" : identified_post,
#         "post_tags" : identified_post.tags.all()
#     })



class ReadLaterView(View):

    def post(self,request):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST['post_id'])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect('/')

    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}
        if stored_posts is None or len(stored_posts)==0:
            context['has_posts'] = False
            context['posts'] = []
        else:
            context['has_posts']=True            
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
        return render(request,"blog/stored-posts.html",context)
        

