from django.shortcuts import render
from django.http import HttpResponse
from unabjj.forms import ContactForm

from django.core.mail import send_mail

from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template, render_to_string
import os



def index(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_phone = request.POST.get('contact_phone', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'form_content': form_content,
            }

            template = render_to_string('contact_template.txt', context)
            # content = template.render(context)

            try:

                email = send_mail(
                    "New contact form submission",
                    template,
                    # from
                    contact_email,
                    # to
                    ['unabjj+TESTING@gmail.com'],
                )
            except Exception as e:
                print(e)


            return redirect('index')

    return render(request, 'dist/landing_page.html', {
        'form': form_class,
    })
