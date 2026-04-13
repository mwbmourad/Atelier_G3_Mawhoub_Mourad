from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Bienvenue dans l'application Banque")