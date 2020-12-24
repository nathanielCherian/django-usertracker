from django.db import models

class Monitor(models.Model):
    url_slug = models.SlugField()
    ip = models.CharField(max_length=20)
    