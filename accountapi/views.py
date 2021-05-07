from rest_framework import viewsets , permissions , filters , generics , exceptions
from .serializer import UserSerializer , FriendSerializer
from django.contrib.auth import get_user_model
from accounts.models import Friend
from .permissions import UpdateOwnProfile

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """ add update and selete user """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','first_name','last_name',)

    """ only own user can change them profile 
    but any user can register """
    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.AllowAny]
        elif self.action in ['list']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [UpdateOwnProfile]
        return [permission() for permission in permission_classes]


class FriendList(generics.ListAPIView):
    """ show list user friend """

    serializer_class = FriendSerializer

    def get_queryset(self):
        user = self.request.user
        relation = Friend.objects.filter( from_user = user )
        return relation


class Follow(generics.CreateAPIView):
    """ follow user by pk """
    serializer_class = FriendSerializer

    def get_queryset(self):
        user = self.request.user
        follow_target = get_user_model().objects.get( pk = self.kwargs['pk'] )
        check_exist = Friend.objects.filter(from_user=user,to_user=follow_target)
        return check_exist

    def perform_create(self,serializer):
        user = self.request.user
        follow_target = get_user_model().objects.get( pk = self.kwargs['pk'] )
        if not self.get_queryset().exists():
            serializer.save( from_user = user , to_user = follow_target )
        else:
            raise exceptions.ValidationError("You already follow this user")


class UnFollow(generics.RetrieveDestroyAPIView):
    """ unfollow by pick user pk """
    serializer_class = FriendSerializer

    def get_object(self):
        user = self.request.user
        follow_target = get_user_model().objects.get( pk = self.kwargs['pk'] )
        check_exist = Friend.objects.get(from_user=user,to_user=follow_target)
        return check_exist
            

    def delete(self,request,*args,**kwargs):
        if self.get_object().exists():
            return self.destroy(request,*args,**kwargs)
        else:
            return exceptions.ValidationError('This user not your friend')





