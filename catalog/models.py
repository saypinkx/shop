from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class CatalogModel(models.Model):
    categories = [
        ('T-shirts', 'T-shirts'),
        ('Hodies', 'Hodies'),
        ('Tops', 'Tops'),
        ('Trousers', 'Trousers')

    ]
    sizes = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(choices=categories)
    size = MultiSelectField(choices=sizes, max_length=20)
    structure = models.CharField()
    def __str__(self):
        return f'{self.name} - {self.category}'

class ImageModel(models.Model):
    product = models.ForeignKey(CatalogModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='imgs')
