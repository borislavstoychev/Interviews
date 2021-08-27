from django.urls import path
from tool import views

urlpatterns = [
    path('', views.CandidateListCreate.as_view(), name='candidate'),
    path('<int:candidate_id>', views.CandidateUpdateDelete.as_view(), name='update and delete')
]