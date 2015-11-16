# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReviewProcess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('competencies', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
                ('percentages', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
            ],
        ),
    ]
