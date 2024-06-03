from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import create_order_mensual,create_order_annual,capture_order,generateAccessToken
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.conf import settings
import stripe
from django.shortcuts import redirect
from rest_framework import status


class CrearOrdenAnnually(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        order = create_order_annual('Productos')
        print("====")
        print(order['id'])
        return Response(order,status=status.HTTP_200_OK)
    

class CrearOrdenMonthly(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        order = create_order_mensual('Productos')
        print("====")
        #print(order['id'])
        return Response(order,status=status.HTTP_200_OK)

# Create your views here.

class CapturarOrder(APIView):
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwargs):
        print("=========>",request.data)
        try:
            order_id = request.data['orderID']
            response = capture_order(order_id)
            print(response)
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error capture_order'})
        
stripe.api_key = settings.STRIPE_API_KEY

@permission_classes([AllowAny])
class MonthlySubscriptionCheckoutView(APIView):
    def post(self, request):
        monthly_subscription_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1PFTaf2LhUMquGOjgihkXmvi',
                    'quantity': 1,
                },
            ],
            payment_method_types=['card',],
            mode='payment', 
            success_url= settings.ALLOWED_HOST_PRODUCTION  + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
            cancel_url= settings.ALLOWED_HOST_PRODUCTION  + '/?canceled=true',
        )
        return redirect(monthly_subscription_session.url, code=303)

@permission_classes([AllowAny])
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
                mode='payment',
                success_url= settings.ALLOWED_HOST_PRODUCTION  + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.ALLOWED_HOST_PRODUCTION  + '/?canceled=true',
            )
            return redirect(annual_subscription_session.url, code=303)
        except Exception as e:
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )