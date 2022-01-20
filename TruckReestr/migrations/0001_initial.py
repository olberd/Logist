# Generated by Django 4.0 on 2022-01-19 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('passport_ser', models.CharField(max_length=10, verbose_name='Серия паспорта')),
                ('passport_no', models.CharField(max_length=10, verbose_name='Номер паспорта')),
                ('passport_issued', models.CharField(max_length=150, verbose_name='Паспорт кем выдан')),
                ('passport_date', models.DateField(verbose_name='Паспорт дата выдачи')),
                ('driver_license_ser', models.CharField(max_length=10, verbose_name='Серия ву')),
                ('driver_license_no', models.CharField(max_length=20, verbose_name='Номер ву')),
                ('driver_license_date', models.DateField(verbose_name='Дата ву')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_auto', models.CharField(max_length=20, verbose_name='Номер машины')),
                ('type_auto', models.CharField(max_length=50, verbose_name='Тип машины')),
                ('brand_auto', models.CharField(max_length=50, verbose_name='Марка машины')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_date', models.DateField(verbose_name='Дата погрузки')),
                ('trip_time', models.TimeField(verbose_name='Время подачи')),
                ('trip_from', models.CharField(max_length=255, verbose_name='Место погрузки')),
                ('trip_to', models.CharField(max_length=255, verbose_name='Место выгрузки')),
                ('type_auto', models.CharField(max_length=50, verbose_name='Вид ТС')),
                ('trip_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена рейса')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TruckReestr.truck')),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TruckReestr.driver')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='number_auto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TruckReestr.truck'),
        ),
    ]