# Generated by Django 4.1.7 on 2023-03-04 19:29

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('avtoapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executors',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='historicalexecutors',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', verbose_name='Номер телефона'),
        ),
    ]
