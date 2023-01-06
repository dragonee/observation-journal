from django.shortcuts import render, redirect

from rest_framework import viewsets

from .serializers import ThreadSerializer, ObservationSerializer
from .models import Thread, Observation

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView

from functools import reduce, partial
from collections import OrderedDict

from itertools import groupby

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


from copy import deepcopy

import datetime


class ObservationFilter(filters.FilterSet):
    class Meta:
        model = Observation
        fields = {
            'pub_date': ('gte', 'lte'),
            'date_closed': ('isnull', ),
        }

class ObservationViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

    filter_backends = [DjangoFilterBackend]
    filter_class = ObservationFilter

class ThreadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows boards to be viewed or edited.
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


def period_from_request(request, days=7, start=None, end=None):
    return (
        request.GET.get('from', start or datetime.date.today() - datetime.timedelta(days=days)),
        request.GET.get('to', end or datetime.date.today() + datetime.timedelta(days=1))
    )


class ObservationListView(ListView):
    model = Observation
    queryset = Observation.objects \
        .filter(date_closed__isnull=True) \
        .select_related('thread', 'type') \
        .prefetch_related('update_set')

    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['open_count'] = len(Observation.objects.filter(date_closed__isnull=True))
        context['closed_count'] = len(Observation.objects.filter(date_closed__isnull=False))

        return context

class ObservationClosedListView(ListView):
    model = Observation
    queryset = Observation.objects \
        .filter(date_closed__isnull=False) \
        .select_related('thread', 'type') \
        .prefetch_related('update_set')

    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['open_count'] = len(Observation.objects.filter(date_closed__isnull=True))
        context['closed_count'] = len(Observation.objects.filter(date_closed__isnull=False))

        return context


def start(request):
    return render(request, "start.html")