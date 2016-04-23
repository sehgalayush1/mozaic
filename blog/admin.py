from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'pub_date', 'category', 'author']
	list_filter = ['pub_date']
	search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)