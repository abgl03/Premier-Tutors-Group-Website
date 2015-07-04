from django.http import Http404
from django.shortcuts import render, get_object_or_404
import datetime
import math

from .models import Tutor, Subject


def index(request):
    tutors_list = Tutor.objects.order_by('first_name')
    subjects_list = Subject.objects.order_by('subject_name')
    context = {'tutors_list': tutors_list, 'subjects_list': subjects_list}
    return render(request, 'tutors/PTG_Tutors.html', context)

def profile(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    tutor_subjects = []
    for subject in tutor.tutorsubject_set.all():
        tutor_subjects += [str(subject)]
    tutor_subjects = ', '.join(tutor_subjects)
    age = datetime.datetime.now().date() - tutor.dob
    age = math.floor(age.days / 365)

    return render(request, 'tutors/PTG_Profile.html', {'tutor': tutor, 'tutor_subjects': tutor_subjects, 'age': age})
