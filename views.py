from django.http import HttpResponse

def home(request):
    return HttpResponse("Bonjour, Django fonctionne parfaitement !")
