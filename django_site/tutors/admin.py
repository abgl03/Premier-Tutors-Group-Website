from django.contrib import admin
from .models import Tutor, Subject, TutorSubject, TutorRole, Role


class SubjectsInline(admin.TabularInline):
    model = TutorSubject

class RolesInLine(admin.TabularInline):
    model = TutorRole

class TutorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['email']}),
        ('Name', {'fields': ['first_name', 'last_name']}),
        ('Profile image', {'fields': ['profile_image']}),
        ('Study Information', {'fields': ['degree', 'university', 'status_of_study']}),
        ('Other Information', {'fields': ['interests', 'availability', 'dob']}),
        (None, {'fields': ['phone']}),
        (None, {'fields': ['desc']}),
        ('Date information', {'fields': ['start_date']}),
    ]
    inlines = [SubjectsInline, RolesInLine]
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ['last_name']



class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject Name', {'fields': ['subject_name']}),
    ]



class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Role', {'fields': ['role_name']})
    ]


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Tutor, TutorAdmin)



