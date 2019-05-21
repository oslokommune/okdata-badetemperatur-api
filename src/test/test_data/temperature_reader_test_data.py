from src.test.test_data.test_data_utils import dynamodb_item_data, temperature_data

location_id_1, location_id_2 = '8171', '8172'

item_1_sensor = dynamodb_item_data(location_id_1, 'sensor')
item_1_sensor_transformed = temperature_data(location_id_1, 'sensor')

item_1_manual = dynamodb_item_data(location_id_1, 'manual')
item_1_manual_transformed = temperature_data(location_id_1, 'manual')

item_2_sensor = dynamodb_item_data(location_id_2, 'sensor')
item_2_sensor_transformed = temperature_data(location_id_2, 'sensor')

item_2_manual = dynamodb_item_data(location_id_2, 'manual')
item_2_manual_transformed = temperature_data(location_id_2, 'manual')


http_event_no_query_params = {
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

get_all_temperatures_response_body = [
    item_1_sensor_transformed,
    item_1_manual_transformed,
    item_2_sensor_transformed,
    item_2_manual_transformed
]

http_event_with_query_params = {
    'resource': '/',
    'path': '/',
    'httpMethod': 'GET',
    'headers': {},
    'queryStringParameters': {
        'location': location_id_1
    },
    'pathParameters': None,
    'stageVariables': None,
    'requestContext': {},
    'body': None,
    'isBase64Encoded': False
}

get_temperature_response_body = [
    item_1_manual_transformed,
    item_1_sensor_transformed
]
