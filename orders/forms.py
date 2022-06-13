from django import forms
from localflavor.sg.forms import SGNRICFINField,SGPostCodeField
from .models import Order

class OrderCreateForm(forms.ModelForm):
    postal_code = SGPostCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
