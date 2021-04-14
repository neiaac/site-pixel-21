from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.


class EmbedVideo(models.Model):
    video = EmbedVideoField()  # same like models.URLField()