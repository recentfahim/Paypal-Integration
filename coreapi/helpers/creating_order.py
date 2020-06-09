from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalhttp import HttpError
from .config import configuration


# Get data
def get_data():
    request = OrdersCreateRequest()

    request.prefer('return=representation')
    request.request_body(
        {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": "100.00"
                    }
                }
            ]
        }
    )

    return request


# Create order
def create_order():
    try:
        client = configuration()
        request = get_data()
        response = client.execute(request)
        print('Order With Complete Payload:')
        print('Status Code:', response.status_code)
        print('Status:', response.result.status)
        print('Order ID:', response.result.id)
        print('Intent:', response.result.intent)
        print('Links:')
        approve_link = ''
        print(response.result.links[1].href)
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            if link.rel == 'approve':
                approve_link = link.href

        return response.result.id, approve_link

    except IOError as ioe:
        print(ioe)
        if isinstance(ioe, HttpError):
            # Something went wrong server-side
            print(ioe.status_code)
