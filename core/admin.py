from django.contrib import admin
from .models import Guild, Character


@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'founded_at')
    search_fields = ('name', 'region')


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'character_class', 'guild')
    list_filter = ('character_class', 'guild')
    search_fields = ('name',)
