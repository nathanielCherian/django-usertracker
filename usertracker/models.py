from django.db import models
from django.urls import reverse
import random
import string

class Monitor(models.Model):
    redirect = models.CharField(max_length=50, blank=False)
    url_slug = models.SlugField()
    full_url = models.CharField(max_length=50)
    activated = models.BooleanField(default=False)
    ip = models.CharField(max_length=20)
    
    def save(self):
        letters = string.ascii_lowercase
        self.url_slug = ''.join(random.choice(letters) for i in range(10))

        while(Monitor.objects.filter(url_slug=self.url_slug)):
            self.url_slug = ''.join(random.choice(letters) for i in range(10))

        self.full_url = reverse('usertracker', args=[self.url_slug,])
        super().save(self)

    def __str__(self):
        return f"[{self.url_slug} -> {self.redirect}]"