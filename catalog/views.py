from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import CatalogModel


# Create your views here.
class CatalogView(View):
    def get(self, request, category):
        catalog = []
        products = CatalogModel.objects.all()
        for product in products:
            records_image_model = product.imagemodel_set.all()
            imgs = []
            for record in records_image_model:
                imgs.append(record)
            catalog.append((product, imgs))
        data = {
            'catalog': catalog,
        }

        return render(request, 'catalog/catalog.html', context=data)
    def select_products(self):

