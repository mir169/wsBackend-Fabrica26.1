from django.contrib import admin
from .models import EldenCharacter, EldenWeapon, EldenBoss


@admin.register(EldenCharacter)
class EldenCharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'gender', 'location', 'role')
    list_filter = ('race', 'gender', 'role')
    search_fields = ('name', 'location', 'role')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'race', 'gender')
        }),
        ('Detalhes', {
            'fields': ('description', 'quote', 'location', 'role', 'image_url')
        }),
    )


@admin.register(EldenWeapon)
class EldenWeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'weapon_type', 'weight', 'physical_attack')
    list_filter = ('weapon_type',)
    search_fields = ('name', 'weapon_type')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'weapon_type', 'description', 'weight')
        }),
        ('Estatísticas de Ataque', {
            'fields': ('physical_attack', 'magic_attack', 'fire_attack', 'lightning_attack', 'holy_attack')
        }),
        ('Mídia', {
            'fields': ('image_url',)
        }),
    )


@admin.register(EldenBoss)
class EldenBossAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'health')
    list_filter = ('location',)
    search_fields = ('name', 'location')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'location', 'description')
        }),
        ('Estatísticas', {
            'fields': ('health', 'rewards')
        }),
        ('Mídia', {
            'fields': ('image_url',)
        }),
    )
