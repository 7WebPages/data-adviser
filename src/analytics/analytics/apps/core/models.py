from django.db import models


class Provider(models.Model):
    """
    Represents Spiders/Data Providers
    """

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    name = models.CharField(max_length=25)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Provider {0}>'.format(self.name)


class Category(models.Model):
    """
    Represents static category for provider
    """

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    provider = models.ForeignKey(Provider)
    parent_category = models.ForeignKey('self')
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Category {0} {1}>'.format(self.provider.name, self.name)
