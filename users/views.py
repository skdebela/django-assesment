from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
