from rest_framework import serializers

from tool.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        exclude = ('recruiter', )

