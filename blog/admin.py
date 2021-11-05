from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ['title','published_date','created_date','status','author']
    list_filter = ['status']
    # ordering = ['created_date']
    search_fields = ['title']
