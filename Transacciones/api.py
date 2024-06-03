from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import create_order,capture_order,generateAccessToken
from rest_framework.permissions import AllowAny


class CrearOrden(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        order = create_order('Productos')
        print("====")
        #print(order['id'])
        return Response(order,status=status.HTTP_200_OK)

# Create your views here.

class CapturarOrderPaypal(APIView):
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