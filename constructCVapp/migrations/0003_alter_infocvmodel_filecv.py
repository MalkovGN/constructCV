# Generated by Django 4.0.6 on 2022-07-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructCVapp', '0002_alter_infocvmodel_options_infocvmodel_filecv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infocvmodel',
            name='fileCV',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
