from django import forms

class UploadResumeForm(forms.Form):
    resume = forms.FileField()
    # date_uploaded = models.DateTimeField(default=timezone.now, 
    #     help_text=_("Date Time test was taken by the User"),
    #     verbose_name=_("Datetime Test Taken"))
