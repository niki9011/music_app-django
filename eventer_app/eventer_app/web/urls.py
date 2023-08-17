from django.urls import path
from .views import index, profile_create, dashboard, event_create, event_details, event_edit, event_delete, \
    profile_details, profile_edit, profile_delete

"""    • http://localhost:8000/ - home page
    • http://localhost:8000/dashboard/ - dashboard page
    • http://localhost:8000/create/ - create event page
    • http://localhost:8000/details/<id>/ - event details page
    • http://localhost:8000/edit/<id>/ - edit event page
    • http://localhost:8000/delete/<id>/ - delete event page
    • http://localhost:8000/profile/create/ - create profile page
    • http://localhost:8000/profile/details/ - profile details page
    • http://localhost:8000/profile/edit/ - edit profile page
    • http://localhost:8000/profile/delete/ - delete profile page"""

urlpatterns = [
    path('', index, name="index"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/create/', profile_create, name="profile create"),
    path('create/', event_create, name="event create"),
    path('details/<int:pk>/', event_details, name="event details"),
    path('edit/<int:pk>/', event_edit, name="event edit"),
    path('delete/<int:pk>/', event_delete, name="event delete"),
    path('profile/details', profile_details, name="profile details"),
    path('profile/edit', profile_edit, name="profile edit"),
    path('profile/delete', profile_delete, name="profile delete"),

    ]