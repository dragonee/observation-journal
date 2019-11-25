from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'boards', views.BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]