from django.urls import include, path, re_path
from django.views.generic import TemplateView

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'threads', views.ThreadViewSet)
router.register(r'observation-api', views.ObservationViewSet)


urlpatterns = [
    re_path(r'^(?P<thread_id>[a-f0-9\-]+)/$', views.observation_list_open, name='public-observation-list'),
    re_path(r'^(?P<thread_id>[a-f0-9\-]+)/closed/$', views.observation_list_closed, name='public-observation-list-closed'),
    re_path(r'^(?P<thread_id>[a-f0-9\-]+)/add/$', views.observation_edit, name='public-observation-add'),
    re_path(r'^(?P<thread_id>[a-f0-9\-]+)/(?P<observation_id>[a-f0-9\-]+)/$', views.observation_edit, name='public-observation-edit'),

    path('', views.start),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
