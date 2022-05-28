from django.contrib import admin
from django.db import models
from .models import Book,Author,Address,Countries
# Register your models here.


class bookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {'slug':("title",)}
    list_filter = ("author","rating",)
    list_display = ("title","author",)



admin.site.register(Book,bookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Countries)