from django.db import models
from django.contrib.auth.models import User


class infoCVModel(models.Model):
    firstName = models.CharField(max_length=64)
    secondName = models.CharField(max_length=64)
    fileCV = models.FileField(upload_to='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'infoCVModel'
        verbose_name_plural = 'infoCVModels'

    def __str__(self):
        return f'{self.firstName} {self.secondName}'

