# Generated by Django 4.0.1 on 2022-01-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TruckReestr', '0002_alter_trip_driver_alter_trip_truck'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Водитель', 'verbose_name_plural': 'Водители'},
        ),
        migrations.AlterModelOptions(
            name='trip',
            options={'ordering': ['-trip_date', 'trip_time'], 'verbose_name': 'Рейс', 'verbose_name_plural': 'Рейсы'},
        ),
        migrations.AlterModelOptions(
            name='truck',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterField(
            model_name='driver',
            name='passport_date',
            field=models.DateField(verbose_name='дата выдачи'),
        ),
    ]