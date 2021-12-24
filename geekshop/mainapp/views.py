from django.shortcuts import render


def products(request):
    title_name = 'продукты'
    links_menu = [
        {'href': 'products/', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'name': title_name,
        'menu_prod': links_menu,
    }
    return render(request, 'mainapp/products.html', context)
# Create your views here.
