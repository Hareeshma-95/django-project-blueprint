from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Google photos app index.")
# Create your views here.
def photo(request):
    return render(request, 'photos/photo.html')