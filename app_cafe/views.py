from django.shortcuts import render

from app_cafe.models import Hotdog


def index_page(request):
    hotdogs = Hotdog.objects.all()
    return render(request, 'index.html', {'hotdogs': hotdogs})
# Create your  views here.
def hotdog_details_views(request, id):
    hotdog = Hotdog.objects.get(id=id)
    return render(request, 'detail.html', {'hotdog': hotdog})