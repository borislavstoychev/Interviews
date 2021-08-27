from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=20)


class Recruiter(models.Model):
    name = models.CharField(max_length=10)
    level = models.PositiveIntegerField(validators=[MaxValueValidator(5)])


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()
    birth_date = models.DateField()
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(
        Recruiter,
        on_delete=models.CASCADE,
    )


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.FloatField()
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)