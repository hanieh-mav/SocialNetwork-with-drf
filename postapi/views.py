from rest_framework import generics , permissions , exceptions  , mixins
from .serializer import PostSerializer , CommentSerializer , LikeSerializer
from posts.models import Post , Comment
from accounts.models import Friend
from django.shortcuts import get_object_or_404


# Create your views here.
class PostList(generics.ListCreateAPIView):

    """ show list of user's post and user's friend post """

    serializer_class = PostSerializer
    
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
    """ show detail of user's post and user's firend post 
    but only user of each post can delete and update post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


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


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = Post.objects.get( pk = self.kwargs['pk'] )
        return Comment.objects.filter( post = post )

    def perform_create(self,serializer):
        user = self.request.user
        post = Post.objects.get( pk = self.kwargs['pk'] )
        serializer.save( user = user , post = post )


class CommentDelete(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user = self.request.user
        comment = Comment.objects.filter(user=user)
        return comment

   
class ReplyAdd(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self,serializer):
        user = self.request.user
        post = get_object_or_404( Post , pk = self.kwargs['pk_post'] )
        comment = get_object_or_404 ( Comment , pk = self.kwargs['pk_comment'] )
        serializer.save( user = user , post = post , reply = comment , is_reply = True)


class ReplyDelete(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user = self.request.user
        comment = Comment.objects.filter(user=user)
        return comment


class LikeAdd(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self,serializer):
        user = self.request.user
        post = Post.objects.get( pk = self.kwargs['pk'] )
        if user not in post.like.all():
            post.like.add(user)
            serializer.save()
        else:
            raise exceptions.ValidationError('You liked this post')


class LikeDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = LikeSerializer
    

    def perform_destroy(self,serializer):
        user = self.request.user
        post = Post.objects.get( pk = self.kwargs['pk'] )
        if user in post.like.all():
            post.like.remove(user)
            serializer.save()
        else:
            raise exceptions.ValidationError("You haven't like this post")






