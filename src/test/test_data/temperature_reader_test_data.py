import json
from decimal import Decimal

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

item_1_transformed = {
    'name': 'xnb003564354000000000b',
    'location': 'Oslo badetemp  1',
    'value': 22.675046226232894,
    'measureTime': '2019-02-19T12:43:09.000+0000',
    'unit': 'C'
}

item_2_transformed = {
    'name': 'xnb003564354000000000c',
    'location': 'Oslo badetemp  2',
    'value': 22.675046226232894,
    'measureTime': '2019-02-19T12:43:09.000+0000',
    'unit': 'C'
}

get_all_temperatures_ok_response = {
    'statusCode': 200,
    'body': json.dumps([item_1_transformed, item_2_transformed])
}

get_all_temperatures_http_event = {
    'resource': '/',
    'path': '/',
    'httpMethod': 'GET',
    'headers': {},
    'queryStringParameters': None,
    'pathParameters': None,
    'stageVariables': None,
    'requestContext': {},
    'body': None,
    'isBase64Encoded': False
}
