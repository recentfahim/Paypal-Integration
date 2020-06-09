from paypalcheckoutsdk.orders import OrdersCaptureRequest
from paypalhttp import HttpError
from .creating_order import create_order
from .config import configuration


# capturing order
def capture_order(order_id):
    request = OrdersCaptureRequest(order_id=order_id)
    try:
        client = configuration()
        response = client.execute(request)

        order = response.result.id
        return order
    except IOError as ioe:
        if isinstance(ioe, HttpError):
            # Something went wrong server-side
            print(ioe.status_code)
            print(ioe.headers)
            print(ioe)
        else:
            # Something went wrong client side
            print(ioe)
