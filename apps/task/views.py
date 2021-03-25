# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def update_installations():
    import requests
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    print(req)
    #print(req.text)
    print("Actualización finalizada con ÉXITO")

