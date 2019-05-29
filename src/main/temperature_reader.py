import boto3
import json

from boto3.dynamodb.conditions import Key
from copy import deepcopy

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
sensor_data_table = dynamodb.Table('badetemperatur-latest')


def get_all_temperatures(event, context):
    if event['queryStringParameters']:
        key = event['queryStringParameters']['location']
        temperature_item_list = query_for_item(key)
    else:
        temperature_item_list = scan_for_items()

    response_body = list(
        map(lambda item: from_dynamodb_format(item), temperature_item_list)
    )

    return lambda_proxy_response(200, response_body)


def query_for_item(key):
    item = sensor_data_table.query(
        KeyConditionExpression=Key('locationId').eq(key)
    )
    return item['Items']


def scan_for_items():
    items = sensor_data_table.scan()['Items']
    return items


def from_dynamodb_format(item):
    new_item = deepcopy(item)
    new_item['temperature']['value'] = float(new_item['temperature']['value'])
    new_item['location']['latitude'] = float(new_item['location']['latitude'])
    new_item['location']['longitude'] = float(new_item['location']['longitude'])
    new_item.pop('locationId')
    return new_item


def lambda_proxy_response(status_code, response_body):
    return {
        'statusCode': status_code,
        'body': json.dumps(response_body),
        'headers': {
            'Access-Control-Allow-Origin': '*',
        }
    }