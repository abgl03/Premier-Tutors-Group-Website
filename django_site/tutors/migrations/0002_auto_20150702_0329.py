# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='email',
            field=models.CharField(unique=True, max_length=254, default='jas.kang@gmail.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutor',
            name='desc',
            field=models.TextField(verbose_name=''),
        ),
    ]
