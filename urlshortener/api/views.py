from api.serializers import URLSerializer, UsersSerializer
from django.contrib.auth import get_user_model
from links.models import URL
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class URLListView(generics.ListAPIView):
    serializer_class = URLSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return URL.objects.filter(user=current_user)


class URLCreateView(generics.CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    permission_classes = [IsAuthenticated]


class UsersListView(generics.ListAPIView):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = UsersSerializer
