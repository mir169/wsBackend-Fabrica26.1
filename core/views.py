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

from .models import Guild, Character
from .serializers import GuildSerializer, CharacterSerializer
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


class GuildListView(ListView):
    model = Guild
    template_name = 'core/guild_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset


class GuildCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Guild
    fields = ['name', 'region', 'founded_at']
    template_name = 'core/guild_form.html'
    success_url = reverse_lazy('guild-list')

    def test_func(self):
        return self.request.user.is_staff


class GuildDetailView(DetailView):
    model = Guild
    template_name = 'core/guild_detail.html'


class GuildUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Guild
    fields = ['name', 'region', 'founded_at']
    template_name = 'core/guild_form.html'
    success_url = reverse_lazy('guild-list')

    def test_func(self):
        return self.request.user.is_staff


class GuildDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Guild
    template_name = 'core/guild_confirm_delete.html'
    success_url = reverse_lazy('guild-list')

    def test_func(self):
        return self.request.user.is_staff


class CharacterListView(ListView):
    model = Character
    template_name = 'core/character_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset


class CharacterCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Character
    fields = ['name', 'level', 'character_class', 'guild']
    template_name = 'core/character_form.html'
    success_url = reverse_lazy('character-list')

    def test_func(self):
        return self.request.user.is_staff


class CharacterDetailView(DetailView):
    model = Character
    template_name = 'core/character_detail.html'


class CharacterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Character
    fields = ['name', 'level', 'character_class', 'guild']
    template_name = 'core/character_form.html'
    success_url = reverse_lazy('character-list')

    def test_func(self):
        return self.request.user.is_staff


class CharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Character
    template_name = 'core/character_confirm_delete.html'
    success_url = reverse_lazy('character-list')

    def test_func(self):
        return self.request.user.is_staff


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


class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = [IsAdminOrReadOnly]


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAdminOrReadOnly]
