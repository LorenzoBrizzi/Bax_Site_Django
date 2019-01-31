from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template


def Bax(request):
    return render(request, 'Bax/index.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # email ourselfe the submitted contact message

        subject = 'Contact Form Recived'
        from_email = settings.DEFAULT_FORM_EMAIL
        to_email = [settings.DEFAULT_FROM_EMAIL]

        contact_message = "{0}, from {1} with email {2}".format(message, name, email, phone)

        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

        return redirect("/index.html/", {})
    return render(request, 'index.html', {})

