from django.db import models


class Reply(models.Model):
    video_id = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
