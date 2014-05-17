from django.http import HttpResponse

def index(request):
    return HttpResponse("Team says hello world!")
