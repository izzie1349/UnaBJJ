from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the unabjj index.")
    return render(request, 'dist/culinary.html')