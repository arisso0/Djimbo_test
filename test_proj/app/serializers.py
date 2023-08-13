from rest_framework import serializers
from .models import Page, Block


class AllPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["name", "slug"]


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ["name", "video_url", "shows_number"]
