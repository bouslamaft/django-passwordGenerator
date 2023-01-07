from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request , 'generator/home.html')


def password(request):
    #generating password : 

    generatedPass = ''
    charachters = list('abcdefghijklmnpqrstuvwxtz')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIKLMNPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        charachters.extend(list('0123456789'))
    if request.GET.get('special'):
        charachters.extend(list('!@#$%^&*()'))
    for x in  range(length):
        generatedPass += random.choice(charachters)
    return render(request ,'generator/password.html' ,{'password' :generatedPass })


#about page 

def about(request):
    return render(request , 'generator/about.html' )

