# Generated by Django 3.1.8 on 2021-11-23 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='video_id',
            field=models.IntegerField(default=0),
        ),
    ]
