from django.contrib.auth import get_user_model
from links.models import URL
from rest_framework import serializers


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['url', 'hash', 'visits_count']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'date_joined', 'last_login']
