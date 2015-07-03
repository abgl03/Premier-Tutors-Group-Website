# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('subject_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('start_date', models.DateTimeField(verbose_name='date joined')),
                ('image_location', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TutorSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('subject', models.ForeignKey(to='tutors.Subject')),
                ('tutor', models.ForeignKey(to='tutors.Tutor')),
            ],
        ),
    ]
