# Generated by Django 4.0.6 on 2022-07-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructCVapp', '0010_infocvmodel_educationsubscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='infocvmodel',
            name='workExperience',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
