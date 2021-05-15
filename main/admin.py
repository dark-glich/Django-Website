from django.contrib import admin
from .models import CommentSection

@admin.register(CommentSection)
class ProductAdmin(admin.ModelAdmin):
    fields = (('name', 'email'), 'comment')
    list_filter = ["email"]
    list_display = ("name", "email")