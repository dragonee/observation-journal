from rest_framework import serializers

from .models import Thread, Observation, ObservationType

from functools import partial

class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'name']


class ObservationSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(
        queryset=ObservationType.objects.all(),
        slug_field='slug'
    )

    thread = serializers.SlugRelatedField(
        queryset=Thread.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Observation
        fields = ['id', 'pub_date', 'thread', 'type', 'situation', 'interpretation', 'approach', 'date_closed']
