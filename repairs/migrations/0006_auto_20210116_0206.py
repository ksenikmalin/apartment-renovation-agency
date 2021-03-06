# Generated by Django 3.1.5 on 2021-01-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0005_remove_services_range_prices'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair_type',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
