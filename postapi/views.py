from rest_framework import generics , permissions , response , status , exceptions
from .serializer import PostSerializer
from posts.models import Post
from accounts.models import Friend
from django.shortcuts import get_object_or_404


# Create your views here.
class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        posts = list()
        user = self.request.user
        user_post = Post.objects.filter(user=user)
        friends = Friend.objects.filter(from_user=user)
        for person in friends:
            friend_post = Post.objects.filter(user=person.to_user)
            for post in friend_post:
                posts.append(post)

        for post in user_post:
            posts.append(post)
        
        return posts

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        post = get_object_or_404(Post,pk=self.kwargs['pk'])
        friend = Friend.objects.filter( from_user= user , to_user = post.user )
        if friend or post.user == user:
            return post


    def perform_update(self,serializer):
        post = Post.objects.filter(pk = self.kwargs['pk'],user=self.request.user)
        if post.exists():
            serializer.instance.user = self.request.user
            serializer.save()
        else:
            raise exceptions.ValidationError("this isn't your post to update:)")


    def delete(self,request,*args,**kwargs):
        post = Post.objects.filter(pk = kwargs['pk'],user=request.user)
        if post.exists():
            return self.destroy(request,*args,**kwargs)
        else:
            raise exceptions.ValidationError("this isn't your post to delete:)")

       

    
        
    