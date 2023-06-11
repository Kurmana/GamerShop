from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about', about),
    path('video', video),
    path('contact', contact),
    path('remot', remot),
    path('product', product),
    path('product/<int:id>', get_product),
]