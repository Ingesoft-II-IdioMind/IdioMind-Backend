from django.urls import path
from .api import CrearOrdenAnnually,CrearOrdenMonthly,CapturarOrder,MonthlySubscriptionCheckoutView,AnnualSubscriptionCheckoutView

urlpatterns = [
    path('api/orders/annual', CrearOrdenAnnually.as_view(),),
    path('api/orders/monthly', CrearOrdenMonthly.as_view(),),
    path('api/orders/capture',CapturarOrder.as_view(),),
    path('checkout/monthly',MonthlySubscriptionCheckoutView.as_view()),
    path('checkout/annual',AnnualSubscriptionCheckoutView.as_view())
]