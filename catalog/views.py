from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class CatalogView(View):
    def get(self, request, category):
        return HttpResponse(f'hello {category}')
