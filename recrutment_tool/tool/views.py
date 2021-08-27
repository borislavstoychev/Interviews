# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from tool.models import Candidate
from tool.serializers import CandidateSerializer


class CandidateListCreate(APIView):
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request):
        candidate_serializer = CandidateSerializer(data=request.data)
        if candidate_serializer.is_valid():
            candidate_serializer.save()
            return Response(candidate_serializer.data, status=201)
        return Response(candidate_serializer.errors, status=400)


class CandidateUpdateDelete(APIView):

    def get(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(id=candidate_id)
            serializer = CandidateSerializer(candidate)
            return Response(serializer.data, status=200)
        except:
            return Response({'message': "Not found"}, status=404)

    def put(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(id=candidate_id)
            serializer = CandidateSerializer(candidate, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=202)
            return Response(serializer.errors, status=404)
        except:
            return Response({'message': "Not found"}, status=404)

    def delete(self, request, candidate_id):
        candidate = Candidate.objects.get(pk=candidate_id)
        candidate.delete()
        return Response(status=204)
