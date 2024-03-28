from django import forms
from seller.models import SellerProduct

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class ProductForm(forms.ModelForm):
    class Meta:
        model = SellerProduct
        fields = ['name','seller','description','price','current_bid','image']