from .models import Monitor

def create_monitor(redirect_url):
    m = Monitor(redirect=redirect_url)
    m.save()
