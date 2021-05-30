from django.contrib.auth import views
from django.urls import path
from .views import (ProfileView , ProfileUpdate , follow , unfollow , register , PasswordChange ,
UserPassReset ,
PassWordResetDone,
PasswordResetConfirm,
PasswordResetComplete)

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]

urlpatterns +=[
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>/page/<int:page>',ProfileView.as_view(),name='profile'),
    path('profile/update/<int:pk>',ProfileUpdate.as_view(),name='profile-update'),
    path('following/<int:pk>',follow,name='follow'),
    path('unfollow/<int:pk>',unfollow,name='unfollow'),
    path('register',register,name='register'),
    
    path('reset/', UserPassReset.as_view(), name='password_reset'),
    path('reset/done/', PassWordResetDone.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/',PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('confirm/done/',PasswordResetComplete.as_view(), name='password_reset_complete'),
]