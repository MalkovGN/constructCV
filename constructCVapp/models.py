from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class infoCVModel(models.Model):
    firstName = models.CharField(max_length=64)
    secondName = models.CharField(max_length=64)
    emailAdress = models.EmailField(blank=True, null=True)
    phoneValidate = RegexValidator(regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$')
    phoneNumber = models.CharField(max_length=12, blank=True, null=True, validators=[phoneValidate])
    gitHubLink = models.URLField(blank=True, null=True)
    socialContacts = models.CharField(max_length=64, blank=True, null=True)
    wantedJobTitle = models.CharField(max_length=64, null=True)
    educationSubscribe = models.TextField(max_length=300, null=True, blank=True)
    fileCV = models.FileField(upload_to='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'infoCVModel'
        verbose_name_plural = 'infoCVModels'

    def __str__(self):
        return f'{self.firstName} {self.secondName}'

