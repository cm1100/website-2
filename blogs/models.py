from django.db import models

# Create your models here.

class Blog_Category(models.Model):
    blog_category = models.CharField(max_length=200)
    category_summary = models.TextField()


class Blog_Real(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_category = models.ForeignKey(Blog_Category,on_delete=models.SET_NULL,null=True)
    blog_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
