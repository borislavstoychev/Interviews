from django.contrib import admin
from django.urls import path

from notes.note.views import HomeView, CreateNoteView, EditNoteView, DeleteNoteView, DetailNoteView

urlpatterns = [
    path('', HomeView.as_view(), name='home page'),
    path('add/', CreateNoteView.as_view(), name='add note page'),
    path('edit/<int:pk>', EditNoteView.as_view(), name='edit note page'),
    path('delete/<int:pk>', DeleteNoteView.as_view(), name='delete note page'),
    path('details/<int:pk>', DetailNoteView.as_view(), name='details note page'),
]