from django.db import models
from django.utils.text import slugify


class Gu(models.Model):
    # Si_CHOICES = (
    #     ('SEOUL', '서울특별시'),
    #     ('SEONGNAM', '성남시')
    # )
    name = models.CharField(max_length=50)
    # si = models.CharField(choices=Si_CHOICES)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="위도")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="경도")

    def save(self):
        self.slug = slugify(self.name)
        super(Gu, self).save()

    def __str__(self):
        return '%s' % self.name


    def __str__(self):
        return self.name
