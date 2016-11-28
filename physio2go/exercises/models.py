from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

class Program(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    duration = models.CharField(_('duration'), max_length=100)

    def __str__(self):
        return self.user.name + "'s Program"

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)

        super(Program, self).save()

class Exercise(models.Model):
    program = models.ForeignKey('Program')
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    dosage = models.CharField(_('dosage'), max_length=100)
    schedule = models.CharField(_('schedule'), max_length=100)
    video = models.FileField(upload_to = u'video/', max_length=200)

    def __str__(self):
        return self.name + ' for ' + self.program.user.name + "'s Program"

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)

        super(Exercise, self).save()

class ProgramEntry(models.Model):
    program = models.ForeignKey('Program')
    date = models.DateTimeField()

class ExerciseEntry(models.Model):
    program_entry = models.ForeignKey('ProgramEntry')
    exercise = models.ForeignKey('Exercise')
    completed = models.BooleanField(default=False)