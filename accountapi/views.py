from rest_framework import viewsets , permissions
from .serializer import UserSerializer
from django.contrib.auth import get_user_model
from .permissions import UpdateOwnProfile

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated,UpdateOwnProfile]
        return [permission() for permission in permission_classes]
