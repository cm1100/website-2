from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic,View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .owner import OwnerListView,OwnerDetailView,OwnerDeleteView,OwnerUpdateView,OwnerCreateView
from .forms import CommentForm
from .models import Forum,Comment

# Create your views here.

class ForumListView(OwnerListView):
    model = Forum
    template_name = "forums/list.html"


class ForumDetailView(OwnerDeleteView):
    model = Forum
    template_name = "forums/detail.html"

    def get(self,request,pk):
        x= Forum.objects.get(id=pk)
        comments = Comment.objects.filter(forum=x).order_by('updated_at')
        comment_form = CommentForm()
        ctx = {"forum":x,"comments":comments,"comment_form":comment_form}
        return render(request,self.template_name,ctx)


class ForumCreateView(OwnerCreateView):
    model = Forum
    fields = ["title","text"]
    template_name = "forums/form.html"

class ForumUpdateView(OwnerUpdateView):
    model = Forum
    fields = ["title","text"]
    template_name = "forums/form.html"

class ForumDeleteView(OwnerDeleteView):
    model = Forum
    template_name = "forums/delete.html"

class CommentCreateView(LoginRequiredMixin,View):
    def post(self,request,pk):
        f = get_object_or_404(Forum,id=pk)
        comment = Comment(text=request.POST["comment"],owner=request.user,forum=f)
        comment.save()
        return redirect(reverse("forums:forum_detail",args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "forums/comment_delete.html"

    def get_success_url(self):
        forum = self.object.forum
        return reverse("forums/forum_detail",args=[forum.id])
