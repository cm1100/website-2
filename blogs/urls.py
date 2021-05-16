from django.contrib import admin
from django.urls import path,include
from . import views

app_name="blogs"

urlpatterns=[
    path("",views.Home.as_view(),name="homepage"),
    path("blog_cat/<int:pk>",views.TitleView.as_view(),name="titles"),
    path("blog/<int:pk>",views.BlogView.as_view(),name="real_blog")
]