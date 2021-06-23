from django import forms

from Petstagram2.core.forms import BootstrapFormMixin
from Petstagram2.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class EditPetForm(PetForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'disabled',
                }
            )
        }