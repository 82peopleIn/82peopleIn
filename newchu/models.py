from django.db import models

# Create your models here.
class Maechul(models.Model):
    gu_title = models.CharField(max_length=10, verbose_name='구')
    dong_title = models.CharField(max_length=10, verbose_name='동')
    classification =  models.CharField(max_length=10, verbose_name='업종')
    prev_year = models.IntegerField(null=True,  verbose_name='작년')
    cur_year = models.IntegerField(null=True,  verbose_name='올해')

    @property
    def mcScore(self):
        return (self.prev_year-self.cur_year)/(self.cur_year * 100)
