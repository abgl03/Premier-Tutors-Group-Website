# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0003_auto_20150702_0405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='image_location',
        ),
    ]
