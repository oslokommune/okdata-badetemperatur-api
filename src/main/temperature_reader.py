import boto3
import json

from boto3.dynamodb.conditions import Key
from copy import deepcopy

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
sensor_data_table = dynamodb.Table('badeball-latest')


def get_all_temperatures(event, context):

    temperature_item_list = scan_for_items()
    response_body = list(
        map(lambda item: from_dynamodb_format(item), temperature_item_list)
    )

    return lambda_proxy_response(200, response_body)


def get_temperature(event, context):
    key = event['pathParameters']['name']
    temperature_item = query_for_item(key)

    response_body = from_dynamodb_format(temperature_item)

    return lambda_proxy_response(200, response_body)


def query_for_item(key):
    item = sensor_data_table.query(
        KeyConditionExpression=Key('lovationId').eq(key)
    )
    return item['Items'].pop()


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


def extract_temperature(sensor_value_list):
    temperature = list(
        filter(lambda sensor_value: sensor_value['type'].lower() == 'temperature', sensor_value_list))

    return float(temperature.pop()['value'])


def lambda_proxy_response(status_code, response_body):
    return {
        'statusCode': status_code,
        'body': json.dumps(response_body)
    }