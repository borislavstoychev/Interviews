from django.urls import path, include
from tool import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('candidates', views.CandidatesViewSet)
router.register('jobs', views.JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recruiters/', views.RecruiterView.as_view(), name="recruiters")
    # path('', views.CandidateListCreate.as_view(), name='candidate'),
    # path('<int:candidate_id>', views.CandidatesViewSet.as_view(), name='update and delete')
]