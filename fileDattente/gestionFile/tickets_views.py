

from django.http import HttpResponse
from django.shortcuts import render
from .models import ClientQueueManager


def tickets(request):
    return HttpResponse('salut tickets')


def addClientSImple(request):
    ClientQueueManager.add_client()
    return render(request, 'accueil.html')


def addClientSenior(request):
    ClientQueueManager.add_senior()
    return render(request, 'accueil.html')


def addClientPregnant(request):
    ClientQueueManager.add_pregnant()
    return render(request, 'accueil.html')
