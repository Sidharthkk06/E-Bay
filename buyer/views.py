from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.sellerprofile  # Assuming you have a SellerProfile linked to the User
            product.save()
            return redirect('seller_product_list')  # Redirect to product list view
    else:
        form = ProductForm()
    return render(request, 'seller/add_product.html', {'form': form})
