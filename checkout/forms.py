from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """ Creates a custom form for the Order model """
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address_1",
            "street_address_2",
            "postcode",
            "city",
            "county",
            "country",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "street_address_1": "Street Address 1",
            "street_address_2": "Street Address 2",
            "postcode": "Postcode",
            "city": "City",
            "county": "County",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            # self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
