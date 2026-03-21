from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'guilds', views.GuildViewSet)
router.register(r'characters', views.CharacterViewSet)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('guilds/', views.GuildListView.as_view(), name='guild-list'),
    path('guilds/new/', views.GuildCreateView.as_view(), name='guild-create'),
    path('guilds/<int:pk>/', views.GuildDetailView.as_view(), name='guild-detail'),
    path('guilds/<int:pk>/edit/', views.GuildUpdateView.as_view(), name='guild-update'),
    path('guilds/<int:pk>/delete/', views.GuildDeleteView.as_view(), name='guild-delete'),

    path('characters/', views.CharacterListView.as_view(), name='character-list'),
    path('characters/new/', views.CharacterCreateView.as_view(), name='character-create'),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character-detail'),
    path('characters/<int:pk>/edit/', views.CharacterUpdateView.as_view(), name='character-update'),
    path('characters/<int:pk>/delete/', views.CharacterDeleteView.as_view(), name='character-delete'),

    path('eldenring/', views.eldenring_search, name='eldenring-search'),
    path('eldenring/characters/', views.eldenring_characters, name='eldenring-characters'),
    path('eldenring/weapons/', views.eldenring_weapons, name='eldenring-weapons'),
    path('eldenring/bosses/', views.eldenring_bosses, name='eldenring-bosses'),

    # API
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]