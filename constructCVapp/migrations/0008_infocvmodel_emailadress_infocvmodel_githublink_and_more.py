# Generated by Django 4.0.6 on 2022-07-21 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructCVapp', '0007_infocvmodel_filecv'),
    ]

    operations = [
        migrations.AddField(
            model_name='infocvmodel',
            name='emailAdress',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='infocvmodel',
            name='gitHubLink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='infocvmodel',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(regex='^(\\+7|7|8)?[\\s\\-]?\\(?[489][0-9]{2}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{2}[\\s\\-]?[0-9]{2}$')]),
        ),
        migrations.AddField(
            model_name='infocvmodel',
            name='socialContacts',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
