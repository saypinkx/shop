from django.urls import path
from .views import CatalogView
urlpatterns = [
    path('<category>', CatalogView.as_view(), name='catalog'),
]