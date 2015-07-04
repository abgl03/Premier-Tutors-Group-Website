from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Tutor, Subject


def index(request):
    tutors_list = Tutor.objects.order_by('first_name')
    subjects_list = Subject.objects.order_by('subject_name')
    context = {'tutors_list': tutors_list, 'subjects_list': subjects_list}
    return render(request, 'tutors/PTG_Tutors.html', context)

def profile(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    return render(request, 'tutors/PTG_Profile.html', {'tutor': tutor})
