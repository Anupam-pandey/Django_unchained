from django.contrib import admin
from .models import Post,Tag, Author, Comment

# Register your models here.




class PostAdmin(admin.ModelAdmin):
    list_filter = ('author','date', 'tags',)
    list_display = ('author','date', 'title',)
    prepopulated_fields = {"slug": ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name','text','post',)


admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)