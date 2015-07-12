from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls.static import settings
from . import views


urlpatterns = [
    # ex: /tutors/
    url(r'^$', views.index, name='tutors'),
    url(r'^(?P<tutor_id>[0-9]+)$', views.profile, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)