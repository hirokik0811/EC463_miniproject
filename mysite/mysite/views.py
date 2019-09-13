'''
Created on Sep 13, 2019

@author: kwibu
'''
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')