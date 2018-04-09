# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osr', '0002_auto_20180328_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programeligibility',
            options={'verbose_name_plural': 'program eligibilities'},
        ),
        migrations.AddField(
            model_name='eligibility',
            name='colour',
            field=models.CharField(default=b'#000000', max_length=50),
        ),
        migrations.AddField(
            model_name='offering',
            name='dow',
            field=models.CharField(default=b'Tuesday', max_length=50),
        ),
        migrations.AddField(
            model_name='outcome',
            name='colour',
            field=models.CharField(default=b'#000000', max_length=50),
        ),
        migrations.AddField(
            model_name='program',
            name='colour',
            field=models.CharField(default=b'#000000', max_length=50),
        ),
        migrations.AlterField(
            model_name='program',
            name='img_src1',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='program',
            name='img_src2',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='program',
            name='img_src3',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='program',
            name='img_src4',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='program',
            name='img_txt1',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='img_txt2',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='img_txt3',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='img_txt4',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='intro1',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='program',
            name='intro2',
            field=models.TextField(blank=True, default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='program',
            name='video',
            field=models.CharField(blank=True, default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='img_src',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
