from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Post , Comment
from accounts.models import Friend

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser :
            self.fields = ['image','status','description','user']
        else:
            self.fields = ['image','status','description']   
        return super().dispatch(request, *args, **kwargs)


class FormValid():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
        return super().form_valid(form)    


class AccessUser():
    def dispatch(self, request,pk, *args, **kwargs):
        post = get_object_or_404(Post,pk=pk)
        if post.user == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("you can not edit this post")


class DeletePostAccess():
    def dispatch(self,request,pk, *args, **kwargs):
        post = get_object_or_404(Post,pk=pk)
        comment = Comment.objects.filter(post=post)
        if post.user == request.user or comment.user == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can not Delete this comment")
          




