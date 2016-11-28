from __future__ import unicode_literals

from django.apps import AppConfig


class ExercisesConfig(AppConfig):
    name = 'physio2go.exercises'
    verbose_name = "Exercise Programs"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
