# Generated by Django 4.1.1 on 2022-09-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ManyToManyField(to='jobs.job', verbose_name='Job'),
        ),
    ]
