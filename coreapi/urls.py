from django.urls import path
from .views import CreateOrder, CaptureOrder


urlpatterns = [
    path('create-order/', CreateOrder.as_view(), name='create_order'),
    path('capture-order/', CaptureOrder.as_view(), name='capture_order'),
]
