from django.shortcuts import render


# Create your views here.



from django.http import HttpResponse





def index(request):
    return HttpResponse("Hello, world. You're at the youtube app index.")
# Create your views here.

def home(request):
    return render(request, 'youtube/home.html')
