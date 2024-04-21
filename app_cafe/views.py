from django.shortcuts import render

from app_cafe.models import Hotdog, Drink


def index_page(request):
    hotdogs = Hotdog.objects.all()
    return render(request, 'index.html', {'hotdogs': hotdogs})


# Create your  views here.
def hotdog_details_views(request, id):
    hotdog = Hotdog.objects.get(id=id)
    return render(request, 'detail.html', {'hotdog': hotdog})


def index_page_two(request):
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'drinks': drinks})


def drink_details_views(request, id):
    drink = Drink.objects.get(id=id)
    return render(request, 'detail.html', {'drink': drink})
