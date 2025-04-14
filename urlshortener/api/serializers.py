from django.contrib.auth import get_user_model
from links.models import URL
from rest_framework import serializers


class URLListSerializer(serializers.ModelSerializer):
    """
    Serializer for getting a list of saved URLs.
    """
    class Meta:
        model = URL
        fields = ['user', 'url', 'hash', 'visits_count']


class URLShortenSerializer(serializers.ModelSerializer):
    """
    Serializer for shortening a new URL.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = URL
        fields = ['url', 'user']


class UsersSerializer(serializers.ModelSerializer):
    """
    Serializer for users.
    """
    class Meta:
        model = get_user_model()
        fields = ['username', 'date_joined', 'last_login']
