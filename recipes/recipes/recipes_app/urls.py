from django.urls import path

from recipes.recipes_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home page'),
    path('create/', views.CreateView.as_view(), name='create recipe page'),
    path('edit/<int:pk>', views.EditView.as_view(), name='edit recipe page'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete recipe page'),
    path('details/<int:pk>', views.DetailsView.as_view(), name='recipe details page'),
]