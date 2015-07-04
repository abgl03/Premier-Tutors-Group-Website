# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0009_auto_20150702_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('role_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TutorRole',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('role', models.ForeignKey(to='tutors.Role')),
            ],
        ),
        migrations.AddField(
            model_name='tutor',
            name='availability',
            field=models.CharField(max_length=20, default='Limited'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='degree',
            field=models.TextField(verbose_name='Degree', default='Bachelor of Science Double Majoring in Computer Science and Information Systems'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='dob',
            field=models.DateField(verbose_name='Date of Birth', default=datetime.datetime(2015, 7, 4, 2, 27, 46, 819076, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='interests',
            field=models.TextField(verbose_name='Interests', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='status_of_study',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='university',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutorrole',
            name='tutor',
            field=models.ForeignKey(to='tutors.Tutor'),
        ),
    ]
