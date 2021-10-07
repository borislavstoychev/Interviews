# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import viewsets, status
from tool.models import Candidate, Job, Recruiter, Skills, Interview
from tool.serializers import CandidateSerializer, JobSerializer, RecruiterSerializer


def skills_checker(data, candidate_or_job):
    for skill in data['skills']:
        if not Skills.objects.filter(name=skill['name']).exists():
            new_skill = Skills(name=skill['name'])
            new_skill.save()
            skill = new_skill
        skill_obj = Skills.objects.get(name=skill['name'])
        candidate_or_job.skills.add(skill_obj)
    return candidate_or_job


def recruiter_checker(recruiter):
    recruiters = Recruiter.objects.all()
    if not recruiters.filter(username=recruiter).exists():
        new_recruiter = Recruiter(username=recruiter)
        new_recruiter.save()
    else:
        rec = recruiters.get(username=recruiter)
        rec.level += 1
        rec.save()


class CandidatesViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        new_candidate = Candidate.objects.create(first_name=data['first_name'],
                                                 last_name=data['last_name'],
                                                 email=data['email'],
                                                 bio=data['bio'],
                                                 birth_date=data['birth_date'],
                                                 recruiter=data['recruiter'],
                                                 )
        new_candidate.save()
        skills_checker(data, new_candidate)
        serializer = CandidateSerializer(new_candidate)
        headers = self.get_success_headers(serializer.data)
        recruiter_checker(serializer.data['recruiter'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        candidates = [Candidate.objects.filter(skills=skill) for skill in serializer.data['skills']]
        for candidate in candidates:
            interview = Interview(job_id=serializer.data['id'], candidate=candidate[0], recruiter=candidate[0].recruiter)
            interview.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RecruiterView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

    def get_queryset(self):
        if self.request.query_params:
            level = self.request.query_params.get('level')
            queryset = Recruiter.objects.filter(level=level)
        else:
            queryset = Recruiter.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# class CandidateListCreate(APIView):
#     def get(self, request):
#         candidates = Candidate.objects.all()
#         serializer = CandidateSerializer(candidates, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         candidate_serializer = CandidateSerializer(data=request.data)
#         if candidate_serializer.is_valid():
#             candidate_serializer.save()
#             return Response(candidate_serializer.data, status=201)
#         return Response(candidate_serializer.errors, status=400)
#
#
# class CandidateUpdateDelete(APIView):
#
#     def get(self, request, candidate_id):
#         try:
#             candidate = Candidate.objects.get(id=candidate_id)
#             serializer = CandidateSerializer(candidate)
#             return Response(serializer.data, status=200)
#         except:
#             return Response({'message': "Not found"}, status=404)
#
#     def put(self, request, candidate_id):
#         try:
#             candidate = Candidate.objects.get(id=candidate_id)
#             serializer = CandidateSerializer(candidate, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=202)
#             return Response(serializer.errors, status=404)
#         except:
#             return Response({'message': "Not found"}, status=404)
#
#     def delete(self, request, candidate_id):
#         candidate = Candidate.objects.get(pk=candidate_id)
#         candidate.delete()
#         return Response(status=204)
