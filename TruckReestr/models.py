from django.db import models
# Create your models here.
from django.urls import reverse


class Files(models.Model):
    name = models.CharField(verbose_name='Название док-та', blank=True, null=True, max_length=50)
    doc = models.FileField(upload_to='documents', blank=True, null=True)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, blank=True, null=True, related_name='docs')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Trip(models.Model):
    trip_date = models.DateField(verbose_name="Дата погрузки", null=True, blank=True)
    trip_time = models.TimeField(verbose_name="Время подачи", null=True, blank=True)
    trip_from = models.CharField(verbose_name="Место погрузки", max_length=255, null=True, blank=True)
    trip_to = models.CharField(verbose_name="Место выгрузки", max_length=255, null=True, blank=True)
    type_auto = models.CharField(verbose_name="Вид ТС", max_length=50, null=True, blank=True)
    trip_cost = models.DecimalField(verbose_name="Цена рейса", max_digits=10, decimal_places=2, null=True, blank=True)
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE, null=True, blank=True)
    truck = models.ForeignKey("Truck", on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('TripDetailView', args=[self.id])

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
        ordering = ['-trip_date', 'trip_time']


class Driver(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=100)
    passport_ser = models.CharField(verbose_name="Серия паспорта", default='', max_length=10, blank=True)
    passport_no = models.CharField(verbose_name="Номер паспорта", default='', max_length=10, blank=True)
    passport_issued = models.CharField(verbose_name="Паспорт кем выдан", default='', max_length=150, blank=True)
    passport_date = models.DateField(verbose_name="дата выдачи", default='', null=True, blank=True)
    driver_license_ser = models.CharField(verbose_name="Серия ву", default='', max_length=10, blank=True)
    driver_license_no = models.CharField(verbose_name="Номер ву", default='', max_length=20, blank=True)
    driver_license_date = models.DateField(verbose_name="Дата ву", default='', null=True, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=20, default='', null=True, blank=True)
    number_auto = models.ForeignKey("Truck", on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('DriverDetailView', args=[self.id])

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ['name']


class Truck(models.Model):
    number_auto = models.CharField(max_length=20, verbose_name="Номер машины", null=True, blank=True)
    type_auto = models.CharField(max_length=50, verbose_name="Тип машины")
    brand_auto = models.CharField(max_length=50, verbose_name="Марка машины")

    def __str__(self):
        return self.number_auto

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Клиент")
    name_full = models.CharField(max_length=255, verbose_name="Клиент")
    is_our = models.BooleanField(auto_created=False)
    trips = models.ForeignKey("Trip", on_delete=models.CASCADE, null=True, blank=True)

