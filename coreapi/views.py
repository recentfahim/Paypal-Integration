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

