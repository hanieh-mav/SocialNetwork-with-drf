from django.shortcuts import render , get_object_or_404  , redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Post , Comment
from accounts.models import Friend , User
from django.views.generic import (ListView , CreateView , UpdateView , DeleteView , DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (
    FieldMixin,
    FormValid,
    AccessUser, 
    )
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import CommentForm
from django.core.paginator import Paginator
# Create your views here.

@login_required
def PostList(request,page=1):
    friends = Friend.objects.filter(from_user=request.user)
    user_post = Post.objects.filter(user=request.user,status='p')
    post = list()
    for person in friends:
        posts = Post.objects.filter(user=person.to_user ,status='p')
        for each in posts:
            post.append(each)
        
    for us_p in user_post:
        post.append(us_p)
    
    paginator = Paginator(post,5)
    posts = paginator.get_page(page)
    context = {
        'post':posts,
    }

    return render(request,'posts/post_list.html',context)


def PostDetail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    friend = Friend.objects.filter(from_user=request.user , to_user=post.user)
    if friend or post.user == request.user :
        show_post = post
        comment = Comment.objects.filter(post=post)
    else:
        raise Http404("you not follow this user")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newcm = form.save(commit=False)
            newcm.user = request.user
            newcm.post = post
            newcm.save()
    else:
        form = CommentForm()
    return render(request,'posts/post_detail.html',{'post':show_post,'comment':comment,'form':form})


class PostCreate(FormValid,FieldMixin,LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'posts/post_create_update.html'
    

class PostUpdate(AccessUser,FormValid,FieldMixin,LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'posts/post_create_update.html'
     

class PostDelete(AccessUser,DeleteView):
    model = Post     
    success_url = reverse_lazy('posts:post-list')


def like(request,pk):
    user = request.user
    post = get_object_or_404(Post,pk=pk)
    if user in post.like.all():
        post.like.remove(user)
    else:
        post.like.add(user)    
    return redirect('posts:post-list')

@login_required
def search(request):
    queryset_list = User.objects.all()

    if 'username' in request.GET:
        username = request.GET['username']
        queryset_list = queryset_list.filter(username__icontains=username)

    context = {
        'queryset_list':queryset_list
    }        

    return render(request,'posts/search.html',context)


@login_required
def AddReply(request,pk_post,pk_comment):
    post = get_object_or_404(Post,pk=pk_post)
    comment = get_object_or_404(Comment,pk=pk_comment)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newcm = form.save(commit=False)
            newcm.user = request.user
            newcm.post = post
            newcm.reply = comment
            newcm.is_reply = True
            newcm.save()
            return redirect('posts:detail-post',pk_post)
    else:
        form = CommentForm()
    return render(request,'posts/replycm_loop.html',{'form':form})
    
    
@login_required
def CommentDelete(request,pk_post,pk_comment_delete):
    post = get_object_or_404(Post,pk=pk_post)
    comment = get_object_or_404(Comment,pk=pk_comment_delete)
    if post.user == request.user or comment.user == request.user:
        Comment.objects.filter(pk=pk_comment_delete).delete()
        return redirect('posts:detail-post',pk_post)
    else:
        raise Http404("You can't delete this commnet")


class ArchievePost(LoginRequiredMixin,ListView):
    queryset = Post.objects.filter(status='d')
    template_name = 'posts/archive_post.html'
    paginate_by = 5