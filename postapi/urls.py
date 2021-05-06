from django.urls import path
from .views import (PostList , 
PostDetail , 
CommentList ,
CommentDelete ,
ReplyAdd ,
ReplyDelete , 
LikeAdd ,
LikeDelete)

app_name = 'postapi'

urlpatterns = [
    path('',PostList.as_view(),name='post_list'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('comment/<int:pk>/',CommentList.as_view(),name='commnet_list'),
    path('comment/delete/<int:pk>/',CommentDelete.as_view(),name='commnet_delete'),
    path('reply/<int:pk_post>/<int:pk_comment>/',ReplyAdd.as_view(),name='reply_add'),
    path('reply/delete/<int:pk>/',ReplyDelete.as_view(),name='reply_delete'),
    path('like/<int:pk>/',LikeAdd.as_view(),name='like_add'),
    path('like/delete/<int:pk>/',LikeDelete.as_view(),name='like_delete'),
]