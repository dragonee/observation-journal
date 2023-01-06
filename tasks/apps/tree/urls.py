from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'threads', views.ThreadViewSet)
router.register(r'observation-api', views.ObservationViewSet)


urlpatterns = [

    path('observations/', views.ObservationListView.as_view(), name='observation-list'),
    path('observations/closed/', views.ObservationClosedListView.as_view(), name='observation-list-closed'),

    path('', views.start),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
