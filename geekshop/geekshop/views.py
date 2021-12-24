from django.shortcuts import render


def index(request):
    title_name = 'главная'
    context = {
        'name': title_name,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title_name = 'контакты'
    context = {
        'name': title_name,
    }
    return render(request, 'geekshop/contacts.html', context)
