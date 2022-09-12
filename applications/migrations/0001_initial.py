# Generated by Django 4.1.1 on 2022-09-12 11:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter', models.TextField(verbose_name='Cover Letter')),
                ('selected', models.BooleanField(verbose_name='Application Status')),
                ('applicant', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Applicant')),
            ],
        ),
    ]