from rest_framework import serializers

from links.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['url', 'hash', 'visits_count']
