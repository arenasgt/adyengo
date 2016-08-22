import json
import dateutil.parser
from django.http import JsonResponse, HttpResponseForbidden
from .models import Notification
from .utils import is_valid_ip, get_client_ip, is_notification_item_hmac_valid


def parse_notification(request):

    client_ip = get_client_ip(request)

    if not is_valid_ip(client_ip):
        return False

    data = json.loads(request.body.decode())

    class HmacCalcInvalid(Exception):
        pass

    def get_notification_items(data):
        return [
            i['NotificationRequestItem']
            for i in data.get('notificationItems', [])
        ]

    def save_notification_item(item):

        if not is_notification_item_hmac_valid(item):
            raise HmacCalcInvalid()

        def get_event_date():
            if item.get('eventDate'):
                return dateutil.parser.parse(item.get('eventDate'))

        amount = item.get('amount', {})


        defaults = {
            'ip_address': client_ip,
            'live': data.get('live'),
            'event_code': item.get('eventCode'),
            'psp_reference': item.get('pspReference'),
            'original_reference': item.get('originalReference'),
            'merchant_reference': item.get('merchantReference'),
            'merchant_account_code': item.get('merchantAccountCode'),
            'event_date': get_event_date(),
            'success': item.get('success') in ['true', 'True', True],
            'payment_method': item.get('paymentMethod'),
            'operations': ','.join(item.get('operations', [])),
            'reason': item.get('reason'),
            'payment_amount': amount.get('value'),
            'currency_code': amount.get('currency')
        }
        # Adyen notificatins are likely to be sent twice, hence we use
        # `get_or_create()`.
        #
        # From Adyen integration manual:
        #   A duplicate notification is one where the eventCode and
        #   pspReference fields are the same.
        # Also:
        #    The reference we have assigned to the payment. This is guaranteed to be globally unique and is used
        #    when communicating with us about this payment. For PENDING, ERROR and CANCELLED results the
        #    pspReference may not (yet) be known and will therefore be empty.
        #
        # Then we also need to do a get or create on merchant_reference
        notification, _ = Notification.objects.get_or_create(
                psp_reference=defaults.pop('psp_reference'),
                event_code=defaults.pop('event_code'),
                merchant_reference=defaults.pop('merchant_reference'),
                defaults=defaults)
        return notification

    try:
        return [
            save_notification_item(item)
            for item in get_notification_items(
                json.loads(request.body.decode())
            )
        ]
    except HmacCalcInvalid:
        return False


def notification_valid_response():
    return JsonResponse({'notificationResponse': '[accepted]'})


def notification_invalid_response():
    return HttpResponseForbidden()
