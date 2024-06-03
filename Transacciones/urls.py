from django.urls import path
from .api import CrearOrden, CapturarOrderPaypal

urlpatterns = [
    path('api/orders', CrearOrden.as_view(),),
    path('api/orders/capture',CapturarOrderPaypal.as_view(),)
]