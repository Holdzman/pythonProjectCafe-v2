from django.shortcuts import render

from app_cafe.models import Hotdog


def index_page(request):
    hotdogs = Hotdog.objects.all()
    return render(request, 'index.html', {'hotdogs': hotdogs})
# Create your  views here.
