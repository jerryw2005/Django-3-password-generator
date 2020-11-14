from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMONPQRSTUVWXYZ"))

    if request.GET.get("numbers"):
        characters.extend(list("123456789"))

    if request.GET.get("special"):
        characters.extend(list("!?@#$%&,.<?:"))

    length = int(request.GET.get("length", 10))
    thepassword = ""
    for x in range(length):
        thepassword = thepassword + random.choice(characters)
    return render(request, 'generator/password.html', {"password" : thepassword})

def aboutpage(request):
    return render(request, 'generator/aboutpage.html')
