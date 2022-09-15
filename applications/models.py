from django.db import models
from applicants.models import User
from jobs.models import Job
from django.utils.translation import gettext_lazy as _

class Application(models.Model):
    applicant = models.ForeignKey(User, verbose_name=_("Applicant"), on_delete=models.CASCADE)
    job = models.ForeignKey(Job, verbose_name=_("Job"), on_delete=models.CASCADE)
    cover_letter = models.TextField(_("Cover Letter"))
    selected = models.BooleanField(_("Application Status"))

    class Meta:
        # 1 Applicant per job application
        unique_together = ('applicant', 'job')

    def __str__(self):
        return f'{self.applicant.email} -- {self.job.role} at {self.job.company}'
