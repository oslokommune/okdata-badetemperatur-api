import json
import base64
from decimal import Decimal

event_data_1 = {
    'deviceId': 'xnb003564354000000000b', 'deviceName': 'Oslo badetemp  1', 'time': '2019-02-19T12:43:09.000+0000',
    'sensors': [
        {'type': 'Reference Voltage', 'value': 2.847015380859375, 'unit': 'V'},
        {'type': 'Battery Voltage', 'value': 4.1386962890625, 'unit': 'V'},
        {'type': 'Air Temperature', 'value': 22.23035400390625, 'unit': 'C'},
        {'type': 'Temperature', 'value': 22.675046226232894, 'unit': 'C'}
    ]
}

event_data_2 = {
    'deviceId': 'xnb003564354000000000c', 'deviceName': 'Oslo badetemp  2', 'time': '2019-02-19T12:43:09.000+0000',
    'sensors': [
        {'type': 'Reference Voltage', 'value': 2.847015380859375, 'unit': 'V'},
        {'type': 'Battery Voltage', 'value': 4.1386962890625, 'unit': 'V'},
        {'type': 'Air Temperature', 'value': 22.23035400390625, 'unit': 'C'},
        {'type': 'Temperature', 'value': 22.675046226232894, 'unit': 'C'}
    ]
}

item_1 = {
    'deviceId': 'xnb003564354000000000b', 'deviceName': 'Oslo badetemp  1', 'time': '2019-02-19T12:43:09.000+0000',
    'sensors': [
        {'type': 'Reference Voltage', 'value': Decimal('2.847015380859375'), 'unit': 'V'},
        {'type': 'Battery Voltage', 'value': Decimal('4.1386962890625'), 'unit': 'V'},
        {'type': 'Air Temperature', 'value': Decimal('22.23035400390625'), 'unit': 'C'},
        {'type': 'Temperature', 'value': Decimal('22.675046226232894'), 'unit': 'C'}
    ]
}

item_2 = {
    'deviceId': 'xnb003564354000000000c', 'deviceName': 'Oslo badetemp  2', 'time': '2019-02-19T12:43:09.000+0000',
    'sensors': [
        {'type': 'Reference Voltage', 'value': Decimal('2.847015380859375'), 'unit': 'V'},
        {'type': 'Battery Voltage', 'value': Decimal('4.1386962890625'), 'unit': 'V'},
        {'type': 'Air Temperature', 'value': Decimal('22.23035400390625'), 'unit': 'C'},
        {'type': 'Temperature', 'value': Decimal('22.675046226232894'), 'unit': 'C'}
    ]
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
