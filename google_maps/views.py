from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse





def index(request):
    return HttpResponse("Hello, world. You're at the Google map app index.")
# Create your views here.
def map(request):
    return render(request, 'maps/map.html')