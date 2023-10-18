from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    """
    This class creates a form based on the Contact class

    It allows users to submit a request directly via the website.
    Their request will be saved in the database.
    """

    class Meta:
        model = Contact
        exclude = ["answered", ]
