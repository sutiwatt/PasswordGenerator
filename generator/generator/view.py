from django.http import HttpResponse
# from django.template import loader  
from django.shortcuts import render
import random

def home(request):
  return render(request, "home.html")

def password(request):
  lowercase = 'abcdefghijklmnopqrstuvwxyz'
  charactor = list(lowercase)
  Uppercase = lowercase.upper()
  include_special = list('!@#$%^&*()')
  number = list('1234567890')
  if request.GET.get('include-special'):
    charactor.extend(include_special)
  if request.GET.get('include-lower-upper'):
    charactor.extend(Uppercase)
  if request.GET.get('number'):
    charactor.extend(number)

  lenght = int(request.GET.get('length'))
  
  

  thepassword = ''
  for i in range(lenght):
    thepassword += random.choice(charactor)


  return render(request,'password.html',{'password':thepassword})