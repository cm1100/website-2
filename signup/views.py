from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.urls import reverse_lazy

# Create your views here.


class UserForm(View):

    def get(self,request):
        form = UserCreationForm()
        ctx = {"form":form}
        return render(request,"signup/signup.html",ctx)


    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect(reverse_lazy("tutorials:homepage"))
        else:
            ctx={"form":form}
            return render(request,"signup/signup.html",ctx)


