from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, PriceForm, ProductPriceFormSet
from .models import *


def home_page(request):
    return render(request, "pages/home.html", )


def about_page(request):
    return render(request, "pages/about.html", )


def product_page(request):
    products = Product.objects.all()

    return render(request, "pages/product.html", {'products': products})


def contact_page(request):
    return render(request, "pages/contact.html", )


def dashboard_page(request):
    products_prices = Product.objects.select_related('price').all()

    context = {
        'products_prices': products_prices

    }
    return render(request, 'pages/dashboard.html', context)


def view_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pages/product_details.html', {'product': product})


def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        price_formset = ProductPriceFormSet(request.POST, instance=Product())

        if product_form.is_valid() and price_formset.is_valid():
            product = product_form.save()
            price_formset.instance = product
            price_formset.save()

            return redirect('dashboard')
    else:
        product_form = ProductForm()
        price_formset = ProductPriceFormSet(instance=Product())

    return render(request, 'pages/create_product.html', {'product_form': product_form, 'price_formset': price_formset})


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    price = product.price

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        price_form = PriceForm(request.POST, instance=price)

        if product_form.is_valid() and price_form.is_valid():
            product_form.save()
            price_form.save()

            return redirect('dashboard')
    else:
        product_form = ProductForm(instance=product)
        price_form = PriceForm(instance=price)

    return render(request, 'pages/update_product.html',
                  {'product_form': product_form, 'price_form': price_form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')

    return render(request, 'pages/delete_product.html', {'product': product})


def productform_page(request):
    return render(request, "pages/productform.html", )
