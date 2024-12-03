from rest_framework import serializers

from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
        )