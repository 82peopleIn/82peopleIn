# Generated by Django 2.2.3 on 2019-09-28 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='생일')),
                ('gender', models.CharField(choices=[('여성', '여성'), ('남성', '남성')], default='', max_length=7, verbose_name='성별')),
                ('in_area', models.PositiveSmallIntegerField(blank=True, choices=[(1, '강남구'), (2, '성동구'), (3, '영등포구'), (4, '광진구'), (5, '마포구'), (6, '송파구')], null=True, verbose_name='관심지역')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]
