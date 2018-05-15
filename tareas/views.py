from django.shortcuts import render

# Create your views here.
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def create_random_user(cantidad):
    for x in range(cantidad):
        username = 'usuario {}'.format(get_random_string(5,string.ascii_letters))
        email = '{}@miempresa.com.co'.format(username)
        password= get_random_string(50)
        User.objects.create_user(username=username,email=email,password=password)
    return '{} usuarios creados correctamente'.format(x)

