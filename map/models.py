from django.db import models

# Create your models here.

class Store(models.Model):

    name = models.CharField(max_length=200, blank=False)
    sector = models.CharField(max_length=20)
    location = models.CharField(max_length=30, verbose_name="소재지")
    code = models.IntegerField()
    latitude = models.DecimalField(max_digits=20, decimal_places=5)
    longitude = models.DecimalField(max_digits=20, decimal_places=5)

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.name)

class Seoul(Store):
    pass

class Bucheon(Store):
    pass


