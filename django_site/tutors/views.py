from django.http import Http404
from django.shortcuts import render, get_object_or_404
import datetime
import math

from .models import Tutor, Subject, TutorSubject


def index(request):
    tutors_list = Tutor.objects.order_by('first_name')
    subjects_list = Subject.objects.order_by('subject_name')
    context = {'tutors_list': tutors_list, 'subjects_list': subjects_list}
    return render(request, 'tutors/PTG_Tutors.html', context)


def profile(request, tutor_id):
    # number of tutors
    number_of_tutors = Tutor.objects.count()

    # get role(s)
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    tutor_roles = []
    for role in tutor.tutorrole_set.all():
        tutor_roles += [str(role)]
    tutor_roles = ', '.join(tutor_roles)
    if tutor_roles:
        tutor_roles = tutor_roles[0] + tutor_roles.lower()[1:]

    # calculate age
    age = datetime.datetime.now().date() - tutor.dob
    age = math.floor(age.days / 365)

    # get related tutors
    list_of_tutors = Tutor.objects.all().order_by('?')
    related = []
    for subject in tutor.tutorsubject_set.all():
        for peer in list_of_tutors:
            for peer_subject in peer.tutorsubject_set.all():
                if subject.subject == peer_subject.subject and peer not in related and peer != tutor:
                    related += [peer]

    return render(request, 'tutors/PTG_Profile.html',
                  {'tutor': tutor,
                   'tutor_roles': tutor_roles,
                   'age': age,
                   'number_of_tutors': number_of_tutors,
                   'related': related
                   })
