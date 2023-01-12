import uuid

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils.text import Truncator

def default_state():
    return []

class Thread(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class ObservationType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Observation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    pub_date = models.DateField(_("Observation date"))

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    type = models.ForeignKey(ObservationType, on_delete=models.CASCADE, help_text=_("What type of observation is it?"))

    situation = models.TextField(help_text=_("What happened?"), null=True, blank=True)
    interpretation = models.TextField(help_text=_("How you saw it, what you felt?"), null=True, blank=True)
    approach = models.TextField(help_text=_("How should you approach it in the future?"), null=True, blank=True)

    date_closed = models.DateField(help_text=_("Optional – set this date whenever you feel the work on this observation is complete."), null=True, blank=True)

    class Meta:
        ordering = ('-pub_date', )

    @property
    def situation_truncated(self):
        return Truncator(self.situation).words(6)

    def __str__(self):
        return "{}: {} ({})".format(
            self.pub_date,
            self.situation_truncated,
            self.thread
        )


class Update(models.Model):
    pub_date = models.DateField(auto_now_add=True)

    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)

    comment = models.TextField(_("Update"))

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.comment
