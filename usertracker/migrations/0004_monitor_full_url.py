# Generated by Django 3.1.4 on 2020-12-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertracker', '0003_monitor_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='full_url',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]