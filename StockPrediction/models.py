# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StockTickers(models.Model):
    sid = models.IntegerField()
    stock_ticker = models.CharField(max_length=10)

    def __str__(self):
        return "Stock ID: {}, Stock Ticker: {}".format(self.sid, self.stock_ticker)

    def save(self, *args, **kwargs):
        super(StockTickers, self).save()


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return "Name: {} {}\nUsername: {}\nEmail: {}".format(self.firstname, self.lastname, self.username, self.email)

    def save(self, *args, **kwargs):
        super(Users, self).save()


class HistoricalStocks(models.Model):
    sid = models.ForeignKey(StockTickers, on_delete=models.CASCADE)
    dat = models.DateField()
    open_value = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close_value = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return "Stock ID: {}, Date: {}, Open Price: {}".format(self.sid, self.dat, self.open_value)

    def save(self, *args, **kwargs):
        super(HistoricalStocks, self).save()

    class Meta:
        ordering = ["-dat"]


class RealTimeStocks(models.Model):
    sid = models.ForeignKey(StockTickers, on_delete=models.CASCADE)
    dat = models.DateField()
    time = models.TimeField()
    open_value = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close_value = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return "Stock ID: {}, Date: {}, Time: {} Open Price: {}".format(self.sid, self.dat, self.time, self.open_value)

    def save(self, *args, **kwargs):
        super(RealTimeStocks, self).save()

    class Meta:
        ordering = ["-dat", "-time"]


class Thresholds(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    sid = models.ForeignKey(StockTickers, on_delete=models.CASCADE)
    open_value = models.ForeignKey(HistoricalStocks, on_delete=models.CASCADE)
    threshold = models.IntegerField()

    def __str__(self):
        return "Username: {}, Stock ID: {}, Threshold Percentage: {}".format(self.username, self.sid, self.threshold)

    def save(self, *args, **kwargs):
        super(Thresholds, self).save()
