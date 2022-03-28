from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings

from website.forms import ContactUs
from .models import Profile,Work     # , SiteManager

# Create your views here.


def index(request):
    try:
        profile = Profile.objects.all()
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")

    try:
        work = Work.objects.all()
    except Work.DoesNotExist:
        raise Http404("Work does not exist")


    context = {
        'profile': profile,
        'work': work,
    }


    form = ContactUs(request.POST or None)
    if form.is_valid():
        subject = 'Subject:' + form.cleaned_data['subject']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        message = form.cleaned_data['message']
        recipient_list = [settings.EMAIL_HOST_USER]
        email_message = EmailMessage(subject, message, from_email, recipient_list, reply_to=[email])
        try:
            email_message.send()
        except BadHeaderError:
            return HttpResponse('Un en-tête non valide a été détecté.')



    return render(request, "base.html",context)