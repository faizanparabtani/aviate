from django.db import models
from applicants.models import User
from jobs.models import Job
from django.utils.translation import gettext_lazy as _

class Application(models.Model):
    applicant = models.ManyToManyField(User, verbose_name=_("Applicant"))
    job = models.ManyToManyField(Job, verbose_name=_("Job"))
    cover_letter = models.TextField(_("Cover Letter"))
    selected = models.BooleanField(_("Application Status"))

    def __str__(self):
        return f'{self.applicant.first().email} -- {self.job.first().role} at {self.job.first().company}'
