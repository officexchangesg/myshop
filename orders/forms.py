from django import forms
from .models import Order
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
<<<<<<< HEAD
=======

>>>>>>> 25b485f6fc3721598feb5a080a8516f3d539e28f
