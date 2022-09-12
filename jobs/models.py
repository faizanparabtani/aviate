from django.db import models
from companies.models import Company
from multiselectfield import MultiSelectField


#Skills on the platform
skills = (
    ('python', 'Python'),
    ('java', 'Java'),
    ('cpp', 'C++'),
    ('r', 'R')
)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    location = models.CharField(max_length=50)
    skills = MultiSelectField(choices=skills, max_choices=10, max_length=100)

    def __str__(self):
        return f'{self.role} at {self.company}'

