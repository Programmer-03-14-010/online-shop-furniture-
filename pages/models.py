from django.db import models

from common.models import BaseModel


class ContactModel(BaseModel):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

class AboutModel(models.Model):
    name = models.CharField(max_length=128)
    job = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'
