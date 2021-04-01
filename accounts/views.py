from django.shortcuts import render , get_object_or_404 ,redirect
from .models import User , Friend
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AccessUser
from django.views.generic import UpdateView , ListView 
from django.contrib.auth.views import PasswordChangeView
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import login


# Create your views here.


class ProfileUpdate(AccessUser,UpdateView):
    model = User
    template_name = 'registration/profile_update.html'
    fields = ('username','first_name','last_name','email','avatar','bio')


class ProfileView(LoginRequiredMixin,ListView):
    template_name = 'registration/profile.html'

    def get_queryset(self):
        global user , is_folllowing
        pk = self.kwargs.get('pk')
        user = get_object_or_404(User,pk=pk)
        is_folllowing = Friend.objects.filter(from_user=self.request.user , to_user=user).exists()
        return user.posts.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_curr'] = user 
        context['is_folllowing'] = is_folllowing
        return context


def follow(request,pk):
    user = request.user
    get_user = get_object_or_404(User,pk=pk)
    friend = Friend(from_user=user,to_user=get_user)
    check_exist = Friend.objects.filter(from_user=user,to_user=get_user).exists()
    if not check_exist:
        friend.save()
    return redirect('posts:post-list')
    

def unfollow(request,pk):
    user = request.user
    get_user = get_object_or_404(User,pk=pk)
    check_exist = Friend.objects.filter(from_user=user,to_user=get_user).exists()
    if check_exist:
        Friend.objects.get(from_user=user,to_user=get_user).delete()
    return redirect('posts:post-list')
   

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password1'] and cd['password2'] and cd['password1'] == cd['password2']:
                user = User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password1'])
                user.save()
                login(request,user)
                messages.success(request,'You Registered successfully You can complete your info in your profile','success')
                return redirect('posts:post-list')
            else:
                messages.error(request,'Passwords must be match','danger')
                return redirect('accounts:register')
    else:
        form = RegisterUserForm()
    return render(request,'registration/register.html',{'form':form})
                       

class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('accounts:password_change_done')
