from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('eldenring/', views.eldenring_search, name='eldenring-search'),
    path('eldenring/characters/', views.eldenring_characters, name='eldenring-characters'),
    path('eldenring/weapons/', views.eldenring_weapons, name='eldenring-weapons'),
    path('eldenring/bosses/', views.eldenring_bosses, name='eldenring-bosses'),

    # CRUD Elden Ring Database
    path('elden/characters/', views.EldenCharacterListView.as_view(), name='elden-character-list'),
    path('elden/characters/new/', views.EldenCharacterCreateView.as_view(), name='elden-character-create'),
    path('elden/characters/<int:pk>/', views.EldenCharacterDetailView.as_view(), name='elden-character-detail'),
    path('elden/characters/<int:pk>/edit/', views.EldenCharacterUpdateView.as_view(), name='elden-character-update'),
    path('elden/characters/<int:pk>/delete/', views.EldenCharacterDeleteView.as_view(), name='elden-character-delete'),

    path('elden/weapons/', views.EldenWeaponListView.as_view(), name='elden-weapon-list'),
    path('elden/weapons/new/', views.EldenWeaponCreateView.as_view(), name='elden-weapon-create'),
    path('elden/weapons/<int:pk>/', views.EldenWeaponDetailView.as_view(), name='elden-weapon-detail'),
    path('elden/weapons/<int:pk>/edit/', views.EldenWeaponUpdateView.as_view(), name='elden-weapon-update'),
    path('elden/weapons/<int:pk>/delete/', views.EldenWeaponDeleteView.as_view(), name='elden-weapon-delete'),

    path('elden/bosses/', views.EldenBossListView.as_view(), name='elden-boss-list'),
    path('elden/bosses/new/', views.EldenBossCreateView.as_view(), name='elden-boss-create'),
    path('elden/bosses/<int:pk>/', views.EldenBossDetailView.as_view(), name='elden-boss-detail'),
    path('elden/bosses/<int:pk>/edit/', views.EldenBossUpdateView.as_view(), name='elden-boss-update'),
    path('elden/bosses/<int:pk>/delete/', views.EldenBossDeleteView.as_view(), name='elden-boss-delete'),

    # API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]