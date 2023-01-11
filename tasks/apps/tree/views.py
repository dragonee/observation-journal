from django.shortcuts import render, redirect
from datetime import date

from rest_framework import viewsets

from .serializers import ThreadSerializer, ObservationSerializer
from .models import ObservationType, Thread, Observation, Update
from .forms import ThreadForm, ObservationForm

from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.forms import inlineformset_factory

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


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


def start(request):
    if request.method == "POST":
        form = ThreadForm(request.POST)
    
        if form.is_valid():
            thread = form.save()
            return redirect(reverse('public-observation-list', kwargs={'thread_id': thread.id }))

    else:
        form = ThreadForm()

    return render(request, "start.html", {
        "form": form
    })


def observation_list(request, thread_id, is_open):
    thread = get_object_or_404(Thread, id=thread_id)

    object_list = Observation.objects \
        .filter(thread=thread) \
        .filter(date_closed__isnull=is_open) \
        .select_related('thread', 'type') \
        .prefetch_related('update_set') \
        .order_by('-pub_date')
    
    open_count = len(Observation.objects.filter(date_closed__isnull=True, thread=thread))
    closed_count = len(Observation.objects.filter(date_closed__isnull=False, thread=thread))

    return render(request, "tree/observation_list.html", {
        'object_list': object_list,
        'open_count': open_count,
        'closed_count': closed_count,
        'thread': thread,
        'is_closed_view': not is_open,
    })


def observation_list_open(request, thread_id):
    return observation_list(request, thread_id, is_open=True)


def observation_list_closed(request, thread_id):
    return observation_list(request, thread_id, is_open=False)


def observation_edit(request, thread_id=None, observation_id=None):
    thread = get_object_or_404(Thread, id=thread_id)

    if observation_id is not None:
        observation = get_object_or_404(Observation, id=observation_id, thread=thread)        
    else:
        observation = Observation(thread=thread)

    UpdateFormSet = inlineformset_factory(Observation, Update, fields=('comment',))

    if request.method == "POST":
        form = ObservationForm(request.POST, instance=observation)
        formset = UpdateFormSet(request.POST, instance=observation)
    
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse('public-observation-list', kwargs={'thread_id': thread.id }))

    else:
        form = ObservationForm(instance=observation, initial={
            'pub_date': date.today(),
            'type': ObservationType.objects.first(),
        })
        formset = UpdateFormSet(instance=observation)

    return render(request, "tree/observation_edit.html", {
        "form": form,
        "formset": formset,
        "instance": observation,
        "thread": thread,
        "thread_as_link": True,
    })
