# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0010_auto_20150704_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='user',
        ),
    ]
