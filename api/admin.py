from django.contrib import admin
from .models import PostIt


@admin.register(PostIt)
class PostItModel(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    ordering = ('title', 'description')
