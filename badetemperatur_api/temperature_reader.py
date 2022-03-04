import json
import logging

from badetemperatur_api.temperature_table import TemperatureTable


logger = logging.getLogger()
logger.setLevel(logging.INFO)

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

    temperature_table = TemperatureTable()

    if location:
        temperature_item_list = temperature_table.query_for_item(location)
    else:
        temperature_item_list = temperature_table.scan_for_items()

    response_body = list(
        filter(
            lambda item: filter_source(item, data_sources),
            map(TemperatureTable.from_dynamodb_format, temperature_item_list),
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


def lambda_proxy_response(status_code, response_body):
    return {
        "statusCode": status_code,
        "body": json.dumps(response_body),
        "headers": {"Access-Control-Allow-Origin": "*"},
    }
