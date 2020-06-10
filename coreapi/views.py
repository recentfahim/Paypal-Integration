from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from coreapi.helpers import config, creating_order, capture_order
from rest_framework import status
from coreapi.helpers.paypal.CaptureIntent import create_order, capture_order


class CreateOrder(APIView):
    def get(self, request):
        order_create = create_order.CreateOrder()
        order_id, approve_link = order_create.create_order()
        # order_id, approve_link = creating_order.create_order()
        context = {
            'order_id': order_id,
            'payment_link': approve_link,
        }
        return Response(context, status=status.HTTP_200_OK)


class CaptureOrder(APIView):

    def get(self, request):
        params = request.query_params
        order_id = params.get('token')
        order_capture = capture_order.CaptureOrder()
        response = order_capture.capture_order(order_id=order_id)
        if response.status_code == 201:
            context = {
                'message': "Payment Successful"
            }

            return Response(context, status=status.HTTP_200_OK)

        context = {
            "message": "Payment unsuccessful"
        }
        return Response(context, status=status.HTTP_406_NOT_ACCEPTABLE)

