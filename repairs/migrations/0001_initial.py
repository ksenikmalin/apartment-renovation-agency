# Generated by Django 3.1.5 on 2021-01-15 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call_application_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naimenovaniye', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Статус заявки на обратный звонок',
                'verbose_name_plural': 'Статусы заявок на обратный звонок',
            },
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_days', models.CharField(max_length=150, verbose_name='Количетво дней от/до')),
            ],
            options={
                'verbose_name': 'Продолжительность',
                'verbose_name_plural': 'Продолжительности',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naimenovaniye', models.CharField(max_length=150, verbose_name='Наименование')),
                ('image', models.ImageField(null=True, upload_to='media/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naimenovaniye', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('square', models.CharField(max_length=150, verbose_name='Площадь')),
                ('price', models.IntegerField(verbose_name='Площадь')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Order_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naimenovaniye', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказов',
            },
        ),
        migrations.CreateModel(
            name='Repair_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naimenovaniye', models.CharField(max_length=150, verbose_name='Наименование')),
                ('cost_of_work', models.IntegerField(verbose_name='Стоимость вида работы за кв/м')),
            ],
            options={
                'verbose_name': 'Вид работы',
                'verbose_name_plural': 'Виды работы',
            },
        ),
        migrations.CreateModel(
            name='Type_of_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naimenovaniye', models.CharField(max_length=150, verbose_name='Наименование')),
                
            ],
            options={
                'verbose_name': 'Тип работы',
                'verbose_name_plural': 'Типы работы',
            },
        ),
        migrations.CreateModel(
            name='Сlient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=150, verbose_name='Отчество')),
                ('number_phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=255, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naimenovaniye', models.CharField(max_length=150, verbose_name='Наименование')),
                ('range_prices', models.CharField(max_length=150, verbose_name='Диапозон цены')),
                ('id_duration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.duration', verbose_name='Продолжительность')),
                ('id_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.object', verbose_name='Объект')),
                ('id_repair_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.repair_type', verbose_name='Вид работы')),
                ('id_type_of_work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.type_of_work', verbose_name='Тип работы')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, verbose_name='текст')),
                ('id_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.сlient', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naimenovaniye', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('id_files', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.files', verbose_name='Файл')),
                ('id_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолия',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='id_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.сlient', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='order',
            name='id_order_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.order_status', verbose_name='Статус заказа'),
        ),
        migrations.AddField(
            model_name='order',
            name='id_services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.services', verbose_name='Услуга'),
        ),
        migrations.CreateModel(
            name='Back_call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('number_phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('id_call_application_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repairs.call_application_status', verbose_name='Статус заявки на обратный звонок')),
            ],
            options={
                'verbose_name': 'Обратный звонок',
                'verbose_name_plural': 'Обратные звонки',
            },
        ),
    ]
