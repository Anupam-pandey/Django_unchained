from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify



# Create your models here.


class Countries(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    def __str__(self):
        return(f"{self.name}")
    
    class Meta:
        verbose_name_plural = "Countries"




class Address(models.Model):
    street = models.CharField(max_length=50)
    postal = models.CharField(max_length=5)
    city =  models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.street} {self.postal} {self.city}")
    
    class Meta:
        verbose_name_plural = "Author address"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=CASCADE ,null=True)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    #author = models.CharField(max_length=50, null=True) #added later  after creation of db
    #author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True, related_name="books")
    is_best_seller = models.BooleanField(default=False)   #added later  after creation of db 
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Countries)

    #slug = models.SlugField(default="", blank=True, editable=False, null=False, db_index=True)


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return(f"{self.author}, {self.slug} ,{self.is_best_seller} ,{self.title} ,{self.rating}")

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    




