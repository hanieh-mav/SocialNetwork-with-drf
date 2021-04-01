from django.urls import path
from .views import (PostList ,
 PostCreate , 
 PostUpdate ,
 PostDelete ,
 like , 
 PostList , 
 search ,
 PostDetail,
 AddReply,
 CommentDelete,
 ArchievePost
 )

app_name = 'posts'
urlpatterns = [
    path('',PostList,name='post-list'),
    path('page/<int:page>',PostList,name='post-list'),
    path('create',PostCreate.as_view(),name='create-post'),
    path('detail/<int:pk>',PostDetail,name='detail-post'),
    path('reply/<int:pk_post>/<int:pk_comment>',AddReply,name='add-reply'),
    path('delete/<int:pk_post>/<int:pk_comment_delete>',CommentDelete,name='delete-comment'),
    path('update/<int:pk>',PostUpdate.as_view(),name='update-post'),
    path('delete/<int:pk>',PostDelete.as_view(),name='delete-post'),
    path('like/<int:pk>',like,name='like'),
    path('search',search,name='search'),
    path('archive',ArchievePost.as_view(),name='archive'),
    path('archive/page/<int:page>',ArchievePost.as_view(),name='archive'),
]