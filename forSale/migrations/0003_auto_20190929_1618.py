# Generated by Django 2.2.3 on 2019-09-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forSale', '0002_auto_20190929_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]
