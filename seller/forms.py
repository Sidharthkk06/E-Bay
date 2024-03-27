from django import forms
from buyer.models import Product

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'starting_bid', 'end_time', 'image']