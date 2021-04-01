from django.contrib.auth import views
from django.urls import path
from .views import ProfileView , ProfileUpdate , follow , unfollow , register , PasswordChange

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns +=[
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>/page/<int:page>',ProfileView.as_view(),name='profile'),
    path('profile/update/<int:pk>',ProfileUpdate.as_view(),name='profile-update'),
    path('following/<int:pk>',follow,name='follow'),
    path('unfollow/<int:pk>',unfollow,name='unfollow'),
    path('register',register,name='register'),
]