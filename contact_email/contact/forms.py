from django.forms import ModelForm
from .models import ContactDetails


class ContactDetailsForm(ModelForm):
    class Meta:
        model = ContactDetails
        fields = '__all__'
