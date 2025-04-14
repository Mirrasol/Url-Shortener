from links.models import URL
from rest_framework import serializers


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['url', 'hash', 'visits_count']
