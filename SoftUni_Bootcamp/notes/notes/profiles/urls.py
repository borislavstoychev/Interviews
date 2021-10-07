from django.urls import path

from notes.profiles.views import CreateProfileView, ProfileView, delete_profile

urlpatterns = [
    path('create', CreateProfileView.as_view(), name='create profile'),
    path('', ProfileView.as_view(), name='profile page'),
    path('delete/<int:pk>', delete_profile, name='delete profile')
]
