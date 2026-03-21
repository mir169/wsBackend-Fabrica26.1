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
    if query:
        try:
            response = requests.get('https://eldenring.fanapis.com/api/creatures', params={'name': query}, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = data.get('data', [])
        except Exception as exc:
            errors = str(exc)

    return render(request, 'core/eldenring_search.html', {
        'query': query,
        'results': results,
        'errors': errors,
    })


class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = [IsAdminOrReadOnly]


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAdminOrReadOnly]
