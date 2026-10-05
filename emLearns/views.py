from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django! This is the home page of the emLearns project.")