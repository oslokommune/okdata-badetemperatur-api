import json
import base64
from src.test.test_data.test_data_utils import dynamodb_item_data, temperature_data


event_data_1_sensor = temperature_data('8171', 'sensor')
item_1_sensor = dynamodb_item_data('8171', 'sensor')

event_data_1_manual = temperature_data('8171', 'manual')
item_1_manual = dynamodb_item_data('8171', 'manual')

event_data_2_sensor = temperature_data('8172', 'sensor')
item_2_sensor = dynamodb_item_data('8172', 'sensor')

event_data_2_manual = temperature_data('8172', 'manual')
item_2_manual = dynamodb_item_data('8172', 'manual')


kinesis_event = {
    'Records': [
        {
            'kinesis': {
                'data': base64.b64encode(json.dumps(event_data_1_sensor).encode('utf-8'))
            }
        },
        {
            'kinesis': {
                'data': base64.b64encode(json.dumps(event_data_2_sensor).encode('utf-8'))
            }
        },
        {
            'kinesis': {
                'data': base64.b64encode(json.dumps(event_data_1_manual).encode('utf-8'))
            }
        },
        {
            'kinesis': {
                'data': base64.b64encode(json.dumps(event_data_2_manual).encode('utf-8'))
            }
        }
    ]
}

b64_encoded_obj = 'ewoia2V5IjogInRoaXMgaXMgYSB0ZXN0Igp9'
obj_decoded = {'key': 'this is a test'}
