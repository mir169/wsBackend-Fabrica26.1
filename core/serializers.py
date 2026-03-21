from rest_framework import serializers
from .models import Guild, Character

class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'