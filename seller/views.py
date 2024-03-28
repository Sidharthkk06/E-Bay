from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View, ListView
from seller.models import SellerProfile, SellerProduct
from django.contrib.auth.forms import UserCreationForm
from seller.forms import SignInForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'seller/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            SellerProfile.objects.create(user=user)
            return redirect('login')  # Redirect to login page after successful registration
        else:
            form = UserCreationForm()
            return render(request, 'seller/register.html', {'form': form})

class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'seller/signin.html', {'form': form})
    
    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_obj = authenticate(request, username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('profile')
        form = SignInForm()
        return render(request, 'seller/signin.html', {'form': form})
    
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            seller_name = request.user.username
        return render(request, 'seller/profile.html', {'seller_name': seller_name})
    
class ProductsView(ListView):
    model = SellerProduct
    template_name = 'seller/products.html'
    context_object_name = 'products'
