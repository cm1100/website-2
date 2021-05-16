from django.shortcuts import render
from django.views import View
from .models import Blog_Category,Blog_Real
# Create your views here.

class Home(View):
    def get(self,request):
        objects = Blog_Category.objects.all()
        ctx = {"objects":objects}
        return render(request,"blogs/list.html",ctx)


class TitleView(View):
    def get(self,request,pk):
        objects = Blog_Real.objects.all()
        objects=objects.filter(blog_category=pk)
        ctx = {"objects":objects}
        return render(request,"blogs/title.html",ctx)


class BlogView(View):
    def get(self,request,pk):
        objects = Blog_Real.objects.all()
        objects = objects.filter(id=pk)
        objects=objects[0]
        ctx = {"objects":objects}
        return render(request,"blogs/blog.html",ctx)

