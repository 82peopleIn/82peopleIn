from django.conf import settings
from django.db import models
from django.urls import reverse
from pytz import timezone


def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)

class Item(models.Model):
    name = models.CharField(max_length=20, verbose_name="상가명")
    location = models.CharField(max_length=30, verbose_name="소재지")
    area = models.CharField(max_length=8,verbose_name="면적")
    sector = models.CharField(max_length=8,verbose_name="현 업종", null = True, blank = True)
    option = models.TextField(verbose_name="옵션", null = True, blank = True)
    tel = models.CharField(max_length=20, verbose_name="부동산 전화번호", null = True, blank = True)
    floor = models.CharField(max_length=5, verbose_name="해당층", null = True, blank = True)
    desc = models.TextField(verbose_name="매물 특징")
    price = models.CharField(max_length=20,verbose_name="가격")
    photo = models.ImageField()  # blank=True 지정하지 않은 경우
    lat = models.DecimalField(null = True, max_digits=15, decimal_places=6)
    lng = models.DecimalField(null = True, max_digits=15, decimal_places=6)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forSale:item_detail', kwargs={'pk': self.pk})

