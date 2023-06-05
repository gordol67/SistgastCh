from django.urls import path
from SGastWebito.CaptaVenta.views import EntradaVieW

urlpatterns = [
    path('', EntradaVieW.as_view(), name='entrada'),
]
