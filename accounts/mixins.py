from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import User


class AccessUser():
    def dispatch(self,request,pk,*args ,**kwargs):
        user = get_object_or_404(User,pk=pk)
        if user == request.user or request.user.is_superuser:
            return super().dispatch(request,*args,*kwargs)
        else:
            raise Http404("You can not see this proflile")



        