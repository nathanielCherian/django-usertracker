from django.db import models
from django.urls import reverse


class Monitor(models.Model):
    redirect = models.CharField(max_length=50, null=False)
    
    url_slug = models.SlugField(unique=True)
    full_url = models.CharField(max_length=50)

    activated = models.BooleanField(default=False)
    ip = models.CharField(null=True, max_length=20)
    time = models.DateTimeField(null=True)
    
    def save(self, *args, **kwargs):
        self.full_url = reverse('usertracker', args=[self.url_slug,])
        super(Monitor, self).save(*args, **kwargs)
    

    def __str__(self):
        return f"[{self.url_slug} -> {self.redirect}]"