from django.urls import path, include
from .views import home, dashboard, profile_create, profile_details, profile_edit, \
    profile_delete, game_create, game_details, game_edit, game_delete

""" • http://localhost:8000/ - home page
    • http://localhost:8000/profile/create - create profiles page
    • http://localhost:8000/dashboard/ - dashboard page
    • http://localhost:8000/game/create/ - create game page
    • http://localhost:8000/game/details/<id>/ - details game page
    • http://localhost:8000/game/edit/<id>/ - edit game page
    • http://localhost:8000/game/delete/<id>/ - delete game page
    • http://localhost:8000/profile/details/ - details profiles page
    • http://localhost:8000/profile/edit/ - edit profiles page
    • http://localhost:8000/profile/delete/ - delete profiles page"""

urlpatterns = [
    path('', home, name="home"),
    path('profiles/create', profile_create, name="profiles create"),
    path('dashboard/', dashboard, name="dashboard"),
    path('game/create/', game_create, name="game create"),
    path('game/details/<int:pk>/', game_details, name="game details"),
    path('game/create/<int:pk>/', game_edit, name="game edit"),
    path('game/delete/<int:pk>/', game_delete, name="game delete"),
    path('profiles/details', profile_details, name="profiles details"),
    path('profiles/edit', profile_edit, name="profiles edit"),
    path('profiles/delete', profile_delete, name="profiles delete"),
]