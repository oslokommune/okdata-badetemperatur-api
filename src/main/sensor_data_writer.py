import json
import base64
import boto3
import logging
from botocore.exceptions import ClientError
from copy import deepcopy
from decimal import Decimal, DecimalException

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
sensor_data_table = dynamodb.Table('badeball-latest')


def handle_event(event, context):
    try:
        list(map(lambda item: put_item(item),
                 map(lambda record_data: to_dynamodb_format(record_data),
                     map(lambda record: b64_to_obj(record['kinesis']['data']), event['Records'])
                     )
                 )
             )
    except ClientError as e:
        logger.exception(f'Something went writing to dynamodb. {e}')
    except KeyError as e:
        logger.exception(f'Something went wrong when parsing event data {e}')
    except DecimalException as e:
        logger.exception(f'Something went wrong when converting float to Decimal. {e}')

def put_item(item):
    logger.info(f'Writing new item to table/badeball-latest: {item}')
    response = sensor_data_table.put_item(
        Item=item
    )
    return response


def to_dynamodb_format(item):
    new_item = deepcopy(item)
    new_item['locationId'] = new_item['location']['id']
    new_item['temperature']['value'] = Decimal(str(new_item['temperature']['value']))
    new_item['location']['latitude'] = Decimal(str(new_item['location']['latitude']))
    new_item['location']['longitude'] = Decimal(str(new_item['location']['longitude']))
    return new_item


def b64_to_obj(b64):
    s = base64.b64decode(b64)
    return json.loads(s)
