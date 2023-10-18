from django.db import models


class Contact(models.Model):
    """This class creates a table to save instances of the contact form."""
    SUBJECT_OPTIONS = [
        ("feedback", "Feedback"),
        ("general", "General"),
        ("subscriptions", "Subscriptions"),
        ("reclamation", "Reclamation"),
        ("product_info", "Information Product"),
    ]

    full_name = models.CharField(max_length=250)
    email = models.EmailField(verbose_name="Email address")
    subject = models.CharField(max_length=150, choices=SUBJECT_OPTIONS)
    message = models.TextField(max_length=700, verbose_name="Your message")
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.email
