# Generated by Django 4.1.5 on 2023-01-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_jobseeker_interview_confirmation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='interview_confirmation',
        ),
    ]
