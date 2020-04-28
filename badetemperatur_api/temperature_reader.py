import boto3
import json
import logging

from boto3.dynamodb.conditions import Key
from copy import deepcopy


logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
sensor_data_table = dynamodb.Table("badetemperatur-latest")


data_sources_default = "manual"
valid_data_sources = ["manual", "sensor"]


def get_all_temperatures(event, context):
    logger.info(event)
    query_params = (
        event["queryStringParameters"] if event["queryStringParameters"] else {}
    )

    location = query_params.get("location")

    data_sources = query_params.get("sources", data_sources_default).split(",")

    if not all(source in valid_data_sources for source in data_sources):
        return lambda_proxy_response(
            400,
            {
                "message": f"Invalid value, source parameter can only contain values: {valid_data_sources}"
            },
        )

    if location:
        temperature_item_list = query_for_item(location)
    else:
        temperature_item_list = scan_for_items()

    response_body = list(
        filter(
            lambda item: filter_source(item, data_sources),
            map(lambda item: from_dynamodb_format(item), temperature_item_list),
        )
    )

    return lambda_proxy_response(200, response_body)


def filter_source(item, sources):
    if sources:
        if item["name"] == "Manuell måling":
            return "manual" in sources
        else:
            return "sensor" in sources
    return False


def query_for_item(key):
    item = sensor_data_table.query(KeyConditionExpression=Key("locationId").eq(key))
    return item["Items"]


def scan_for_items():
    items = sensor_data_table.scan()["Items"]
    return items


def from_dynamodb_format(item):
    new_item = deepcopy(item)
    new_item["temperature"]["value"] = float(new_item["temperature"]["value"])
    new_item["location"]["latitude"] = float(new_item["location"]["latitude"])
    new_item["location"]["longitude"] = float(new_item["location"]["longitude"])
    new_item.pop("locationId")
    return new_item


def lambda_proxy_response(status_code, response_body):
    return {
        "statusCode": status_code,
        "body": json.dumps(response_body),
        "headers": {"Access-Control-Allow-Origin": "*"},
    }
