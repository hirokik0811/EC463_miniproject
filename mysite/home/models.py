'''
Created on Sep 18, 2019

@author: kwibu
'''

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150)
    
    def __str__(self):
        return self.username
        
    class Meta:
        verbose_name_plural = 'users'
    
