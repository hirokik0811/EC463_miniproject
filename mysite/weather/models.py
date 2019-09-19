from django.db import models
from django.apps import apps

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length=25)
	parent_user = models.ForeignKey('home.User', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'cities'
		