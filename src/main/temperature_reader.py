import boto3
import json

from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
sensor_data_table = dynamodb.Table('badeball-latest')


def get_all_temperatures(event, context):

    temperature_item_list = scan_for_items()
    response_body = list(
        map(lambda item: transform_item(item), temperature_item_list)
    )

    return lambda_proxy_response(200, response_body)


def get_temperature(event, context):
    key = event['pathParameters']['name']
    temperature_item = query_for_item(key)

    response_body = transform_item(temperature_item)

    return lambda_proxy_response(200, response_body)


def query_for_item(key):
    item = sensor_data_table.query(
        KeyConditionExpression=Key('deviceId').eq(key)
    )
    return item['Items'].pop()


def scan_for_items():
    items = sensor_data_table.scan()['Items']
    return items


def transform_item(item):
    return {
        'name': item['deviceId'],
        'location': item['deviceName'],
        'value': extract_temperature(item['sensors']),
        'measureTime': item['time'],
        'unit': 'C'
    }


def extract_temperature(sensor_value_list):
    temperature = list(
        filter(lambda sensor_value: sensor_value['type'].lower() == 'temperature', sensor_value_list))

    return float(temperature.pop()['value'])


def lambda_proxy_response(status_code, response_body):
    return {
        'statusCode': status_code,
        'body': json.dumps(response_body)
    }