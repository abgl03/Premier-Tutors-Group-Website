from django.contrib.auth.models import User
from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('tutors/static/profiles', str(instance.id), str(instance.id)+'.jpg')


class Tutor(models.Model):
    user = models.OneToOneField(User, null=True)
    email = models.CharField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    start_date = models.DateTimeField('date joined')
    desc = models.TextField('Description')
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

class Subject(models.Model):
    subject_name = models.CharField(max_length=20)

    def __str__(self):
        return self.subject_name

class TutorSubject(models.Model):
    tutor = models.ForeignKey(Tutor)
    subject = models.ForeignKey(Subject)

    def __str__(self):
        return str(self.subject)


