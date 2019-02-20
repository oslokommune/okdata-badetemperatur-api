import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
temperature_table = dynamodb.Table('badeball-latest')


def get_all_temperatures(event, context):

    item_list = scan_for_items()
    temperature_list = list(
        map(lambda item: transform_item(item), item_list)
    )

    return {
        'statusCode': 200,
        'body': json.dumps(temperature_list)
    }

def scan_for_items():
    items = temperature_table.scan()['Items']
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
        filter(lambda sensor_value: sensor_value['type'].lower() == 'Temperature'.lower(),sensor_value_list))

    return float(temperature[0]['value'])