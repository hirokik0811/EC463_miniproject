from django.db import models
from django.apps import apps

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=25)
    parent_user = models.ForeignKey('home.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'rooms'
        
class TempHumidData(models.Model):
    datetime = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField(0)
    parent_user = models.ForeignKey('home.User', on_delete=models.CASCADE)
    parent_room = models.ForeignKey('Room', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.datetime
    class Meta:
        verbose_name_plural = 'datas'
        
class Interval(models.Model):
    interval = models.IntegerField()
    parent_user = models.ForeignKey('home.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.interval)
    class Meta:
        verbose_name_plural = 'intervals'
    