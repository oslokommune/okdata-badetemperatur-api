import json
import base64
from decimal import Decimal

event_data_1 = {
    "location": {
        "id": "8171",
        "name": "Hovedøya",
        "latitude": 59.893905,
        "longitude": 10.726743
    },
    "name": "Hovedøya brygge",
    "temperature": {
        "value": 4.335,
        "unit": "C"
    },
    "measureTime": "2019-02-19T12:43:09.000+0000"
}

event_data_2 = {
    "location": {
        "id": "8172",
        "name": "Frysja",
        "latitude": 59.893905,
        "longitude": 10.726743
    },
    "name": "Hovedøya brygge",
    "temperature": {
        "value": 4.4,
        "unit": "C"
    },
    "measureTime": "2019-02-19T12:43:09.000+0000"
}

item_1 = {
    "locationId": "8171",
    "location": {
        "id": "8171",
        "name": "Hovedøya",
        "latitude": Decimal('59.89390'),
        "longitude": Decimal('10.72674')
    },
    "name": "Hovedøya brygge",
    "temperature": {
        "value": Decimal('4.34'),
        "unit": "C"
    },
    "measureTime": "2019-02-19T12:43:09.000+0000"
}

item_2 = {
    "locationId": "8172",
    "location": {
        "id": "8172",
        "name": "Frysja",
        "latitude": Decimal('59.89390'),
        "longitude": Decimal('10.72674')
    },
    "name": "Hovedøya brygge",
    "temperature": {
        "value": Decimal('4.40'),
        "unit": "C"
    },
    "measureTime": "2019-02-19T12:43:09.000+0000"
}

kinesis_event = {
    'Records': [
        {
            'kinesis': {
                'data': base64.b64encode(json.dumps(event_data_1).encode('utf-8'))
            }
        },
        {
            'kinesis': {
                'data': base64.b64encode(json.dumps(event_data_2).encode('utf-8'))
            }
        }
    ]
}

b64_encoded_obj = 'ewoia2V5IjogInRoaXMgaXMgYSB0ZXN0Igp9'
obj_decoded = {'key': 'this is a test'}
