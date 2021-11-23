from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
