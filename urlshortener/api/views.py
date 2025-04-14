from api.serializers import URLSerializer, UsersSerializer
from django.contrib.auth import get_user_model
from links.models import URL
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class URLListView(generics.ListAPIView):
    """
    Get a list of shortened URLs, saved by current user.
    """
    serializer_class = URLSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return URL.objects.filter(user=current_user)


class URLCreateView(generics.CreateAPIView):
    """
    Create a new short URL.
    """
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    permission_classes = [IsAuthenticated]


class UsersListView(generics.ListAPIView):
    """
    Get a list of all registered users.
    """
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = UsersSerializer
