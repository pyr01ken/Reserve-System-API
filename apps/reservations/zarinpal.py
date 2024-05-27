"""
    Zarin-pal config
"""
from suds.client import Client
from apps.reservations.models import Reservations

# TODO: Important: need to edit for production.
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/"
ZARINPAL_WEBSERVICE = 'https://sandbox.zarinpal.com/pg/services/WebGate/wsdl'
CallbackURL = 'http://127.0.0.1:8000/payment/verify/'
MERCHANT = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"


def payment_request(amount: int, description: str, order: Reservations,
                    mobile: str = None, email: str = None, ) -> str:
    client = Client(ZARINPAL_WEBSERVICE)
    result = client.service.PaymentRequest(MERCHANT,
                                           amount,
                                           description,
                                           mobile,
                                           email,
                                           CallbackURL)
    if result.Status == 100:
        order.authority = result.Authority
        order.save()
        return ZP_API_STARTPAY + str(order.authority)
    else:
        return error_generator(result.Status)


def payment_verification(amount: int, authority: str) -> tuple:
    client = Client(ZARINPAL_WEBSERVICE)
    result = client.service.PaymentVerification(MERCHANT,
                                                authority,
                                                amount)

    if result.Status == 100:
        return 100, 'Transaction success', result.RefID
    elif result.Status == 101:
        return 101, 'Transaction submitted', None
    else:
        error_generator(result.Status)


def error_generator(status_number: int):
    if status_number == -1:
        raise ZarinpalError('Information submitted is incomplete.')
    elif status_number == -2:
        raise ZarinpalError('Merchant ID or Acceptor IP is not correct.')
    elif status_number == -3:
        raise ZarinpalError('Amount should be above 100 Toman.')
    elif status_number == -4:
        raise ZarinpalError('Approved level of Acceptor is Lower than the silver.')
    elif status_number == -11:
        raise ZarinpalError('Request Not found.')
    elif status_number == -21:
        raise ZarinpalError('Financial operations for this transaction was not found.')
    elif status_number == -22:
        raise ZarinpalError('Transaction is unsuccessful.')
    elif status_number == -33:
        raise ZarinpalError('Transaction amount does not match the amount paid.')
    elif status_number == -34:
        raise ZarinpalError('Limit the number of transactions or number has crossed the divide')
    elif status_number == -40:
        raise ZarinpalError('There is no access to the method.')
    elif status_number == -41:
        raise ZarinpalError('Additional Data related to information submitted is invalid.')
    elif status_number == -54:
        raise ZarinpalError('Request archived.')
    # elif status_number == -101:
    #    raise ZarinpalError('Operation was successful but PaymentVerification \
    #         operation on this transaction have already been done')
    else:
        raise ZarinpalError(f'Un Handled error {status_number}')


# generate specific error for zarinpal
class ZarinpalError(Exception):
    pass
