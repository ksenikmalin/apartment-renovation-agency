# Generated by Django 3.1.5 on 2021-01-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0003_auto_20210115_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='id_type_of_work',
        ),
        migrations.AlterField(
            model_name='repair_type',
            name='type_of_work',
            field=models.CharField(max_length=510, verbose_name='Производимые работы'),
        ),
        migrations.DeleteModel(
            name='Type_of_work',
        ),
    ]
