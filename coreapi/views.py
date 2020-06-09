from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from coreapi.helpers import config, creating_order, capture_order
from rest_framework import status


class CreateOrder(APIView):
    def get(self, request):
        order_id, approve_link = creating_order.create_order()
        context = {
            'order_id': order_id,
            'approve_link': approve_link,
        }
        return Response(context, status=status.HTTP_200_OK)


class CaptureOrder(APIView):

    def get(self, request):
        data = request.data
        params = request.query_params
        print(data)
        print(params)
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        order_id = data.get('order_id') or None

        if order_id:
            capture_order.capture_order(order_id=order_id)
        else:
            context = {
                'message': "Order id not provided"
            }
            return Response(context, status=status.HTTP_406_NOT_ACCEPTABLE)

