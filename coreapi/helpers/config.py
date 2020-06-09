from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from django.conf import settings


# setting up configuration for paypal
def configuration():
    client_id = settings.PAYPAL_CLIENT_ID
    client_secret = settings.PAYPAL_CLIENT_SECRET
    environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment)

    return client
