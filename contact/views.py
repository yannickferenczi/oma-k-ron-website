from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """ This function render the contact form """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data["full_name"]
            email = form.cleaned_data["email"]
            request_subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            subject = "Thank you for your email to Oma K-ron"
            body = render_to_string(
                "contact/email/email_request_received.txt",
                {
                    "full_name": full_name,
                    "request_subject": request_subject,
                    "message": message,
                },
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
            messages.success(
                request,
                "Your request has been successfully submitted!",
            )
            return redirect(reverse("products"))
        else:
            messages.error(
                request,
                "Your form could not be submitted. Please verify your \
                    information.",
            )
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})
