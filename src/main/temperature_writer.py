import json
import base64
import boto3
from copy import deepcopy
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
temperature_table = dynamodb.Table('badeball-latest')


def handle_event(event, context):
    list(map(lambda item: put_item(item),
             map(lambda record_data: float_to_decimal(record_data['data']),
                 map(lambda record: b64_to_obj(record['kinesis']['data']), event['Records'])
                 )
             )
         )


def put_item(item):
    response = temperature_table.put_item(
        Item=item
    )
    return response


def float_to_decimal(item):
    new_item = deepcopy(item)
    for sensor_data in new_item['sensors']:
        sensor_data['value'] = Decimal(str(sensor_data['value']))

    return new_item


def b64_to_obj(b64):
    s = base64.b64decode(b64)
    return json.loads(s)
