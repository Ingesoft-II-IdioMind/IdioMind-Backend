from django.urls import path
from .api import MonthlySubscriptionCheckoutView,AnnualSubscriptionCheckoutView

urlpatterns = [
    path('checkout/monthly',MonthlySubscriptionCheckoutView.as_view()),
    path('checkout/annual',AnnualSubscriptionCheckoutView.as_view())
]