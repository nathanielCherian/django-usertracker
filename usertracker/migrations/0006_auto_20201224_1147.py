# Generated by Django 3.1.4 on 2020-12-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertracker', '0005_auto_20201224_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='is_url',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='url_slug',
            field=models.SlugField(unique=True),
        ),
    ]
