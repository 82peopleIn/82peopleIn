# Generated by Django 2.2.3 on 2019-10-02 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0003_delete_franchise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juicy',
            name='title',
        ),
        migrations.RemoveField(
            model_name='tomntoms',
            name='title',
        ),
    ]
