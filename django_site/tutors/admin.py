from django.contrib import admin
from .models import Tutor, Subject, TutorSubject


class SubjectsInline(admin.TabularInline):
    model = TutorSubject

class TutorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['email']}),
        ('Name', {'fields': ['first_name', 'last_name']}),
        ('Profile image', {'fields': ['profile_image']}),
        (None, {'fields': ['phone']}),
        (None, {'fields': ['desc']}),
        ('Date information', {'fields': ['start_date']}),
    ]
    inlines = [SubjectsInline]
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ['last_name']

admin.site.register(Tutor, TutorAdmin)

class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject Name', {'fields': ['subject_name']}),
    ]

admin.site.register(Subject, SubjectAdmin)



