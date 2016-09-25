from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Picture(models.Model):
    uploader_ip = models.CharField(max_length=15)
    image = models.ImageField(upload_to='uploads/')
    datetime = models.DateTimeField(default=timezone.now)
    title = models.TextField(default='')

    def image_thumbnail(self):
        return '<img style="max-height:100px; max-width:100px;" src="%s"/>' % self.image.url

    image_thumbnail.allow_tags = True

    def report_count(self):
        return Report.objects.filter(picture=self).count()

    def laughing_count(self):
        return Laughing.objects.filter(picture=self).count()

    def fearful_count(self):
        return Fearful.objects.filter(picture=self).count()

    def banana_count(self):
        return Banana.objects.filter(picture=self).count()


class Laughing(models.Model):
    rater_ip = models.CharField(max_length=15)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)


class Fearful(models.Model):
    rater_ip = models.CharField(max_length=15)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)


class Banana(models.Model):
    rater_ip = models.CharField(max_length=15)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)


class Report(models.Model):
    reporter_ip = models.CharField(max_length=15)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)