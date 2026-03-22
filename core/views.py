from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

import requests

from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import EldenCharacter, EldenWeapon, EldenBoss
from .eldenring_api import EldenRingAPI


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


def logout_view(request):
    logout(request)
    return redirect('home')


class HomeView(TemplateView):
    template_name = 'core/home.html'


class LoginView(LoginView):
    template_name = 'core/login.html'


def eldenring_search(request):
    query = request.GET.get('q', '')
    results = []
    errors = None
    api_status = "online"

    if query:
        try:
            results = EldenRingAPI.search_characters(query)
            if not results:
                errors = f"Nenhum personagem encontrado com o nome '{query}'."
        except Exception as exc:
            errors = f"Erro ao buscar na API: {str(exc)}"
            api_status = "offline"
            # Tentar com dados mock
            try:
                results = EldenRingAPI.search_characters(query)
                if results:
                    errors = f"API indisponível. Mostrando dados locais para '{query}'."
            except:
                errors = f"Erro na API e dados locais indisponíveis para '{query}'."

    return render(request, 'core/eldenring_search.html', {
        'query': query,
        'results': results,
        'errors': errors,
        'api_status': api_status,
    })


def eldenring_characters(request):
    """View para listar todos os personagens"""
    characters = []
    errors = None
    api_status = "online"

    try:
        characters = EldenRingAPI.search_characters()  # Sem filtro retorna todos
    except Exception as exc:
        errors = f"Erro ao carregar personagens: {str(exc)}"
        api_status = "offline"

    return render(request, 'core/eldenring_characters.html', {
        'characters': characters,
        'errors': errors,
        'api_status': api_status,
    })


def eldenring_weapons(request):
    """View para listar armas"""
    weapons = []
    errors = None
    api_status = "online"

    try:
        weapons = EldenRingAPI.get_weapons()
    except Exception as exc:
        errors = f"Erro ao carregar armas: {str(exc)}"
        api_status = "offline"

    return render(request, 'core/eldenring_weapons.html', {
        'weapons': weapons,
        'errors': errors,
        'api_status': api_status,
    })


def eldenring_bosses(request):
    """View para listar chefes"""
    bosses = []
    errors = None
    api_status = "online"

    try:
        bosses = EldenRingAPI.get_bosses()
    except Exception as exc:
        errors = f"Erro ao carregar chefes: {str(exc)}"
        api_status = "offline"

    return render(request, 'core/eldenring_bosses.html', {
        'bosses': bosses,
        'errors': errors,
        'api_status': api_status,
    })


# CRUD Views para Elden Ring Entities

class EldenCharacterListView(ListView):
    model = EldenCharacter
    template_name = 'core/elden_character_list.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset


class EldenCharacterCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = EldenCharacter
    fields = ['name', 'race', 'gender', 'description', 'quote', 'location', 'role', 'image_url']
    template_name = 'core/elden_character_form.html'
    success_url = reverse_lazy('elden-character-list')

    def test_func(self):
        return self.request.user.is_staff


class EldenCharacterDetailView(DetailView):
    model = EldenCharacter
    template_name = 'core/elden_character_detail.html'


class EldenCharacterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EldenCharacter
    fields = ['name', 'race', 'gender', 'description', 'quote', 'location', 'role', 'image_url']
    template_name = 'core/elden_character_form.html'
    success_url = reverse_lazy('elden-character-list')

    def test_func(self):
        return self.request.user.is_staff


class EldenCharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EldenCharacter
    template_name = 'core/elden_character_confirm_delete.html'
    success_url = reverse_lazy('elden-character-list')

    def test_func(self):
        return self.request.user.is_staff


class EldenWeaponListView(ListView):
    model = EldenWeapon
    template_name = 'core/elden_weapon_list.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        weapon_type = self.request.GET.get('type')
        if q:
            queryset = queryset.filter(name__icontains=q)
        if weapon_type:
            queryset = queryset.filter(weapon_type=weapon_type)
        return queryset


class EldenWeaponCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = EldenWeapon
    fields = ['name', 'weapon_type', 'description', 'weight', 'physical_attack', 'magic_attack',
              'fire_attack', 'lightning_attack', 'holy_attack', 'image_url']
    template_name = 'core/elden_weapon_form.html'
    success_url = reverse_lazy('elden-weapon-list')

    def test_func(self):
        return self.request.user.is_staff


class EldenWeaponDetailView(DetailView):
    model = EldenWeapon
    template_name = 'core/elden_weapon_detail.html'


class EldenWeaponUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EldenWeapon
    fields = ['name', 'weapon_type', 'description', 'weight', 'physical_attack', 'magic_attack',
              'fire_attack', 'lightning_attack', 'holy_attack', 'image_url']
    template_name = 'core/elden_weapon_form.html'
    success_url = reverse_lazy('elden-weapon-list')

    def test_func(self):
        return self.request.user.is_staff


class EldenWeaponDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EldenWeapon
    template_name = 'core/elden_weapon_confirm_delete.html'
    success_url = reverse_lazy('elden-weapon-list')

    def test_func(self):
        return self.request.user.is_staff


class EldenBossListView(ListView):
    model = EldenBoss
    template_name = 'core/elden_boss_list.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        location = self.request.GET.get('location')
        if q:
            queryset = queryset.filter(name__icontains=q)
        if location:
            queryset = queryset.filter(location=location)
        return queryset


class EldenBossCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = EldenBoss
    fields = ['name', 'location', 'description', 'health', 'rewards', 'image_url']
    template_name = 'core/elden_boss_form.html'
    success_url = reverse_lazy('elden-boss-list')

    def test_func(self):
        return self.request.user.is_staff


class EldenBossDetailView(DetailView):
    model = EldenBoss
    template_name = 'core/elden_boss_detail.html'


class EldenBossUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EldenBoss
    fields = ['name', 'location', 'description', 'health', 'rewards', 'image_url']
    template_name = 'core/elden_boss_form.html'
    success_url = reverse_lazy('elden-boss-list')

    def test_func(self):
        return self.request.user.is_staff


class EldenBossDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EldenBoss
    template_name = 'core/elden_boss_confirm_delete.html'
    success_url = reverse_lazy('elden-boss-list')

    def test_func(self):
        return self.request.user.is_staff
