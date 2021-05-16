from django.contrib import admin
from django.urls import path,include
from . import views
app_name ="tutorials"
urlpatterns = [
    path('',views.HomePage.as_view(),name="homepage"),
    path('series/<int:pk>',views.SeriesView.as_view(),name="series"),
    path("tutorial/<int:pk>",views.TutorialView.as_view(),name="tutorial"),
    path("tutorial/<int:fk>/<int:pk>",views.Tutorial_View_real.as_view(),name="real_tut")
]