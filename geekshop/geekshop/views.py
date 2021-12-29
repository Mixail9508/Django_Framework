from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title_name = 'главная'

    products = Product.objects.all()[:4]

    context = {
        'name': title_name,
        'products': products
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title_name = 'контакты'
    context = {
        'name': title_name,
    }
    return render(request, 'geekshop/contacts.html', context)
