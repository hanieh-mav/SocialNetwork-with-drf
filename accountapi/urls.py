from django.urls import path
from rest_framework import routers
from .views import UserViewSet , FriendList , Follow , UnFollow

router = routers.SimpleRouter()

router.register('user',UserViewSet,basename='user')

urlpatterns = router.urls


urlpatterns = [
    path('friend/',FriendList.as_view(),name='friend_list'),
    path('follow/<int:pk>',Follow.as_view(),name='follow'),
    path('unfollow/<int:pk>',UnFollow.as_view(),name='un_follow'),

]