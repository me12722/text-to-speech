from __future__ import unicode_literals

from django.db import models

class MP3(models.Model):
    file_name = models.CharField(max_length=40)
    text = models.TextField()