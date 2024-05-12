from rest_framework.views import APIView
from idiomind.settings import stripe,ALLOWED_HOST_PRODUCTION 
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response




class MonthlySubscriptionCheckoutView(APIView):
    def post(self, request):
        
            monthly_subscription_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1PFTaf2LhUMquGOjgihkXmvi',  # ID del precio de la suscripción mensual
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment', 
                success_url= ALLOWED_HOST_PRODUCTION  + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= ALLOWED_HOST_PRODUCTION  + '/?canceled=true',
            )
            return redirect(monthly_subscription_session.url, code=303)
        

class AnnualSubscriptionCheckoutView(APIView):
    def post(self, request):
        try:
            annual_subscription_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1PFTa82LhUMquGOjenUsnY5x', 
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment',  # Modo de suscripción en lugar de pago único
                success_url= ALLOWED_HOST_PRODUCTION  + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= ALLOWED_HOST_PRODUCTION  + '/?canceled=true',
            )
            return redirect(annual_subscription_session.url, code=303)
        except Exception as e:
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        

