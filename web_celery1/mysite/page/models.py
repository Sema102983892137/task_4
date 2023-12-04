from django.db import models


class MyUser(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class MyDoctor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    spec = models.CharField(max_length=100, null=True)


class Slot(models.Model):
    doctor = models.ForeignKey(MyDoctor, on_delete=models.PROTECT, blank=True)
    time = models.CharField(max_length=100, null=True)


class ReserveSlot(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.PROTECT, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
    is_two_hours_notice = models.BooleanField(default=False)
    is_one_day_notice = models.BooleanField(default=False)
