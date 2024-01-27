from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

from .models import Post, Category, Comment


class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)

    list_display = ['title', 'author', 'category', 'created']

    search_fields = ['title', 'content']

    list_filter = ['category', 'tags']


admin.site.register(Post, PostAdmin)

admin.site.register(Category)

admin.site.register(Comment)
