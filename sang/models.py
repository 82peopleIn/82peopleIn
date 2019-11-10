from django.db import models
from django.urls import reverse


class Sang(models.Model):
    id = models.IntegerField(primary_key=True)
    gu_title = models.CharField(max_length=10, verbose_name='구')
    dong_title = models.CharField(max_length=10, verbose_name='동')
    living_pop = models.IntegerField(null=True,  verbose_name='거주인구 수')

    def __str__(self):
        return '{} {}: {}'.format(self.gu_title, self.dong_title, self.id)

    def get_absolute_url(self):
        return reverse('sang:sang_detail', kwargs={'pk': self.pk})

