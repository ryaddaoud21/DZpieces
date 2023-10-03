
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django import forms
class ProductForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = '__all__'
        exclude = ('by',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Product Information',
                'name',
                'catalog',
                'brand',
                'price',
                'Product_details',
                'Téléphone',
                'Addresse',
                'image',
            ),
            Submit('submit', 'Publier', css_class='btn btn-primary py-2 px-4'),
        )




class OfferForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = '__all__'
        exclude = ('created_by','created_at','produit',)