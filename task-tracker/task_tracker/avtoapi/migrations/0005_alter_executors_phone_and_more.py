# Generated by Django 4.1.7 on 2023-03-05 10:03

import avtoapi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avtoapi', '0004_alter_executors_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executors',
            name='phone',
            field=models.CharField(max_length=30, validators=[avtoapi.models.validate_phone], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='historicalexecutors',
            name='phone',
            field=models.CharField(max_length=30, validators=[avtoapi.models.validate_phone], verbose_name='Номер телефона'),
        ),
    ]
