# Generated by Django 3.1.5 on 2021-01-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0006_auto_20210116_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
    ]
