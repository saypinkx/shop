from django.contrib import admin
from .models import CatalogModel, ImageModel
# Register your models here.
@admin.register(CatalogModel)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'description', 'size', 'structure']
    list_editable = ['name', 'category', 'price', 'description', 'size', 'structure']
    ordering = ['name']


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']
    list_editable = ['product', 'image']