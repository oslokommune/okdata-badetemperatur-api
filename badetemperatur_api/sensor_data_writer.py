import os
import json
import base64
import boto3
import logging
from botocore.exceptions import ClientError
from copy import deepcopy
from decimal import Decimal, DecimalException

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
sensor_data_table = dynamodb.Table("badetemperatur-latest")


def handle_event(event, context):
    try:
        list(
            map(
                lambda item: put_item(item),
                map(
                    lambda record_data: to_dynamodb_format(record_data),
                    filter(
                        lambda record_data: bool(record_data["temperature"]),
                        map(
                            lambda record: b64_to_obj(record["kinesis"]["data"]),
                            event["Records"],
                        ),
                    ),
                ),
            )
        )
    except ClientError as e:
        logger.exception(f"Something went writing to dynamodb. {e}")
    except KeyError as e:
        logger.exception(f"Something went wrong when parsing event data {e}")
    except DecimalException as e:
        logger.exception(f"Something went wrong when converting float to Decimal. {e}")
    except TypeError as e:
        logger.exception(f"Something went wrong. {e}")


def put_item(item):
    # TODO: remove this check after BYM allows for sensordata in prod, Oyvind Nygard 2020-04-29
    if os.environ["ENV"] == "prod" and item["name"].lower() != "manuell måling":
        return
    logger.info(f"Writing new item to table/badeball-latest: {item}")
    response = sensor_data_table.put_item(Item=item)
    return response


def to_dynamodb_format(item):
    new_item = deepcopy(item)
    new_item["locationId"] = new_item["location"]["id"]
    new_item["temperature"]["value"] = float_to_decimal(
        new_item["temperature"]["value"], num_decimals=2
    )
    new_item["location"]["latitude"] = float_to_decimal(
        new_item["location"]["latitude"], num_decimals=5
    )
    new_item["location"]["longitude"] = float_to_decimal(
        new_item["location"]["longitude"], num_decimals=5
    )
    return new_item


def float_to_decimal(f, num_decimals=None):
    d = Decimal(str(f))
    if num_decimals:
        return round(d, num_decimals)
    else:
        return d


def b64_to_obj(b64):
    s = base64.b64decode(b64)
    obj = json.loads(s)
    logger.info(f"Received data: {obj}")
    return obj
