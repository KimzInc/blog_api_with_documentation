from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Blog API. Visit /api/v1/ for the API.")