from .models import Monitor
import random
import string

def create_monitor(redirect_url):

    letters = string.ascii_lowercase
    url_slug = ''.join(random.choice(letters) for i in range(10))

    while(Monitor.objects.filter(url_slug=url_slug)):
        url_slug = ''.join(random.choice(letters) for i in range(10))


    m = Monitor(redirect=redirect_url, is_url=False, url_slug=url_slug, full_url=full_url)
    m.save()
