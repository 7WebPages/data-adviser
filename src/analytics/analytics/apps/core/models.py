from django.db import models  # noqa


class Provider(models.Model):
    name = models.CharField(max_length=25)
    enabled = models.BooleanField(default=False)


class Category(models.Model):
    provider = models.ForeignKey(Provider)
    parent_category = models.ForeignKey('self')
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=2048, unique=True)
