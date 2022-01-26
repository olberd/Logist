from django.db import models

# Create your models here.
from django.urls import reverse


class Trip(models.Model):
    trip_date = models.DateField(verbose_name="Дата погрузки")
    trip_time = models.TimeField(verbose_name="Время подачи")
    trip_from = models.CharField(verbose_name="Место погрузки", max_length=255)
    trip_to = models.CharField(verbose_name="Место выгрузки", max_length=255)
    type_auto = models.CharField(verbose_name="Вид ТС", max_length=50)
    trip_cost = models.DecimalField(verbose_name="Цена рейса", max_digits=10, decimal_places=2)
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
    truck = models.ForeignKey("Truck", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('TripDetailView', args=[self.id]) # args=[self.id]) #kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
        ordering = ['-trip_date', 'trip_time']


class Driver(models.Model):
    surname = models.CharField(verbose_name="Фамилия", max_length=100)
    name = models.CharField(verbose_name="Имя", max_length=100)
    second_name = models.CharField(verbose_name="Отчество", max_length=100, blank=True)
    passport_ser = models.CharField(verbose_name="Серия паспорта", max_length=10, blank=True)
    passport_no = models.CharField(verbose_name="Номер паспорта", max_length=10, blank=True)
    passport_issued = models.CharField(verbose_name="Паспорт кем выдан", max_length=150, blank=True)
    passport_date = models.DateField(verbose_name="дата выдачи", null=True, blank=True)
    driver_license_ser = models.CharField(verbose_name="Серия ву", max_length=10, blank=True)
    driver_license_no = models.CharField(verbose_name="Номер ву", max_length=20, blank=True)
    driver_license_date = models.DateField(verbose_name="Дата ву", null=True, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=20, null=True, blank=True)
    number_auto = models.ForeignKey("Truck", on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Truck(models.Model):
    number_auto = models.CharField(max_length=20, verbose_name="Номер машины")
    type_auto = models.CharField(max_length=50, verbose_name="Тип машины")
    brand_auto = models.CharField(max_length=50, verbose_name="Марка машины")

    def __str__(self):
        return self.number_auto

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

