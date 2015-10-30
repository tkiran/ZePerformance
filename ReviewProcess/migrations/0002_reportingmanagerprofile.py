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
	    migrations.AlterField(
		model_name='ReportingManagerProfile',
		name='manager',
		field=models.ForeignKey(related_name='rmp_profile', to=settings.AUTH_USER_MODEL),
	    ),
	    migrations.RenameField(
		model_name='ReportingManagerProfile',
		old_name='manager',
		new_name='reporter',
	    ),
    ]
