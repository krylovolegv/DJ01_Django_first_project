from django.contrib import admin
from .models import News_post

class News_postAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'pub_date', 'author')
    list_filter = ['pub_date', 'author']
    search_fields = ['title', 'text']

admin.site.register(News_post, News_postAdmin)