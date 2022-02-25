import os
import logging
from copy import deepcopy
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class TemperatureTable:
    def __init__(self):
        dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
        self.table = dynamodb.Table("badetemperatur-latest")

    def put_item(self, item):
        # TODO: remove this check after BYM allows for sensordata in prod, Oyvind Nygard 2020-04-29
        if os.environ["ENV"] == "prod" and item["name"].lower() != "manuell måling":
            return None
        logger.info(f"Writing new item to table/badetemperatur-latest: {item}")
        response = self.table.put_item(Item=item)
        return response

    def query_for_item(self, key):
        item = self.table.query(KeyConditionExpression=Key("locationId").eq(key))
        return item["Items"]

    def scan_for_items(self):
        items = self.table.scan()["Items"]
        return items

    @staticmethod
    def from_dynamodb_format(item):
        new_item = deepcopy(item)
        new_item["temperature"]["value"] = float(new_item["temperature"]["value"])
        new_item["location"]["latitude"] = float(new_item["location"]["latitude"])
        new_item["location"]["longitude"] = float(new_item["location"]["longitude"])
        new_item.pop("locationId")
        return new_item

    @staticmethod
    def to_dynamodb_format(item):
        new_item = deepcopy(item)
        new_item["locationId"] = new_item["location"]["id"]
        new_item["temperature"]["value"] = TemperatureTable._float_to_decimal(
            new_item["temperature"]["value"], num_decimals=2
        )
        new_item["location"]["latitude"] = TemperatureTable._float_to_decimal(
            new_item["location"]["latitude"], num_decimals=5
        )
        new_item["location"]["longitude"] = TemperatureTable._float_to_decimal(
            new_item["location"]["longitude"], num_decimals=5
        )
        return new_item

    @staticmethod
    def _float_to_decimal(f, num_decimals=None):
        d = Decimal(str(f))
        if num_decimals:
            return round(d, num_decimals)
        else:
            return d
