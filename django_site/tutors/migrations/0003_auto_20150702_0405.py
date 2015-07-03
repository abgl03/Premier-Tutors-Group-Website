# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tutors.models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0002_auto_20150702_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=tutors.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='desc',
            field=models.TextField(verbose_name='Description'),
        ),
    ]
