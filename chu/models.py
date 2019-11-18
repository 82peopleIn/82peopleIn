from django.db import models
from django.urls import reverse


class Chu(models.Model):
    id = models.IntegerField(primary_key=True)
    gu_title = models.CharField(max_length=10, verbose_name='구')
    dong_title = models.CharField(max_length=10, verbose_name='동')
    living_pop = models.IntegerField(null=True,  verbose_name='인구')
    area = models.FloatField(null=True,  verbose_name='km2')
    density = models.IntegerField(null=True, verbose_name='인구밀도')
    high = models.CharField(max_length=10, blank=True, verbose_name='정도')

    def __str__(self):
        return '{} {}: {}'.format(self.gu_title, self.dong_title, self.id)

    def get_absolute_url(self):
        return reverse('chu:chu_detail', kwargs={'pk': self.pk})
