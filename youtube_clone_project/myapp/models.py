from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.ForeignKey('youtube_clone.Comment', on_delete=models.CASCADE)
    reply = models.CharField(max_length=100)
    