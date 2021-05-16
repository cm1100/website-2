from django.contrib import admin
from .models import Blog_Real,Blog_Category
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Blog_Category)
admin.site.register(Blog_Real,BlogAdmin)
