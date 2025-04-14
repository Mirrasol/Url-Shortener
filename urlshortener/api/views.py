from api.serializers import URLSerializer
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
