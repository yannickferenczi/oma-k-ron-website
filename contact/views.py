from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """This function render the contact form"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your form has been successfully submitted!",
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
