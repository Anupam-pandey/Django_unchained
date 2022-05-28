from typing import ClassVar
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE
# Create your models here.



class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Post(models.Model):
    title = models.CharField( max_length=150)
    excerpt = models.CharField(max_length=1000)
    image_name = models.FileField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name="post")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}, {self.author}"




class Comment(models.Model):
    user_name = models.CharField( max_length=150)
    user_email = models.EmailField(max_length=454)
    text = models.TextField()
    post = models.ForeignKey(Post,on_delete=CASCADE, related_name="comments")


