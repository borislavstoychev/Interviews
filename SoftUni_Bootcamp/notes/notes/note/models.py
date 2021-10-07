from django.db import models

# Create your models here.
from notes.profiles.models import Profile


class Notes(models.Model):

    title = models.CharField(max_length=30)
    image_url = models.URLField()
    content = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)