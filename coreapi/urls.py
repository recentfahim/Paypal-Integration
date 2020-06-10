from django.urls import path
from .views import CreateOrder, CaptureOrder, CancelOrder


urlpatterns = [
    path('create-order/', CreateOrder.as_view(), name='create_order'),
    path('capture-order/', CaptureOrder.as_view(), name='capture_order'),
    path('cancel-order/', CancelOrder.as_view(), name='cancel_order'),
]
