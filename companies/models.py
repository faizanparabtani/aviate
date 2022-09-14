from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name="Company Name")
    
    description = models.TextField(verbose_name="Company Description",
    help_text="A brief outline of the functions of the company")

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return str(self.name)