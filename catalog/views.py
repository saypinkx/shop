from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import CatalogModel


# Create your views here.
class CatalogView(View):
    def get(self, request, category):
        data = {
            'product': CatalogModel.objects.all(),

        }
        data['one'] = data['product'][0].imagemodel_set.all()[0].image
        return render(request, 'catalog/catalog.html', context=data)
