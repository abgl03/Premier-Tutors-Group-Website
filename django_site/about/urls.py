from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls.static import settings
from . import views


urlpatterns = [
    # ex: /tutors/
    url(r'^$', views.index, name='tutors'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)