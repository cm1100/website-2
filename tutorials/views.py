from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView
from .models import Tutorial_Category,Tutorial_Series,Tutorial
from django.views import View
from django.urls import reverse_lazy
# Create your views here.





class HomePage(View):
    def get(self,request):
        ctx = {"objects":Tutorial_Category.objects.all()}
        return render(request,"tutorials/homepage.html",ctx)


class SeriesView(View):

    def get(self,request,pk):
        entry = Tutorial_Series.objects.all()
        entry=entry.filter(tut_category=pk)
        ctx={"objects":entry}
        #print("hi i am here")
        return render(request,"tutorials/series.html",ctx)


class TutorialView(View):

    def get(self,request,pk):
        entry = Tutorial.objects.all()
        entry = entry.filter(tut_series=pk)

        entry1=entry[0]
        ctx={"objects":entry,"objects1":entry1}
        return render(request,"tutorials/tutorial.html",ctx)


class Tutorial_View_real(View):

    def get(self,request,fk,pk):
        entry = Tutorial.objects.all()
        entry=entry.filter(tut_series=fk)
        entry1=entry.filter(pk=pk)
        entry1=entry1[0]
        ctx ={"objects":entry,"objects1":entry1}
        return render(request,"tutorials/tutorial.html",ctx)
