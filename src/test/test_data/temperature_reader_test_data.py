import json
from decimal import Decimal

item_1 = {
    "locationId": "8171",
    "location": {
        "id": "8171",
        "name": "Hovedøya",
        "latitude": Decimal('59.893905'),
        "longitude": Decimal('10.726743')
    },
    "name": "Hovedøya brygge",
    "temperature": {
        "value": Decimal('4.3'),
        "unit": "C"
    },
    "measureTime": "2019-02-19T12:43:09.000+0000"
}

item_2 = {
    "locationId": "8172",
    "location": {
        "id": "8172",
        "name": "Hovedøya",
        "latitude": Decimal('59.893905'),
        "longitude": Decimal('10.726743')
    },
    "name": "Hovedøya brygge",
    "temperature": {
        "value": Decimal('4.4'),
        "unit": "C"
    },
    "measureTime": "2019-02-19T12:43:09.000+0000"
}

item_1_transformed = {
    "location": {
        "id": "8171",
        "name": "Hovedøya",
        "latitude": 59.893905,
        "longitude": 10.726743
    },
    "name": "Hovedøya brygge",
    "temperature": {
        "value": 4.3,
        "unit": "C"
    },
    "measureTime": "2019-02-19T12:43:09.000+0000"
}

item_2_transformed = {
    "location": {
        "id": "8172",
        "name": "Hovedøya",
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

http_event_no_path_params = {
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

get_all_temperatures_ok_response = {
    'statusCode': 200,
    'body': json.dumps([item_1_transformed, item_2_transformed])
}

http_event_with_path_params = {
    'resource': '/',
    'path': '/',
    'httpMethod': 'GET',
    'headers': {},
    'queryStringParameters': None,
    'pathParameters': {
        'name': item_1['locationId']
    },
    'stageVariables': None,
    'requestContext': {},
    'body': None,
    'isBase64Encoded': False
}

get_temperature_ok_response = {
    'statusCode': 200,
    'body': json.dumps(item_1_transformed)
}
