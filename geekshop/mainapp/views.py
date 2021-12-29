from django.shortcuts import render

from mainapp.models import Product


def products(request, pk=1):
    print(pk)
    title_name = 'продукты'
    links_menu = [
        {'href': 'products/', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    prod_index = Product.objects.all()[:3]
    context = {
        'name': title_name,
        'menu_prod': links_menu,
        'products': prod_index,
    }
    return render(request, 'mainapp/products.html', context)
# Create your views here.
