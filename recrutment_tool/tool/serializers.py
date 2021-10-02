from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers
from rest_framework.fields import DictField, CharField

from tool.models import Candidate, Job, Skills, Recruiter


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = "__all__"


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = "__all__"
        depth = 1


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = "__all__"
