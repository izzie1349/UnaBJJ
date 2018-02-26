from django.shortcuts import render
from django.http import HttpResponse
from unabjj.forms import ContactForm


def index(request):
    # return HttpResponse("Hello, world. You're at the unabjj index.")
    return render(request, 'dist/landing_page.html')

def contact_form(request):
    form_class = contact_form

    return render(request, 'dist/landing_page.html', {
                            'form': form_class,
    })
