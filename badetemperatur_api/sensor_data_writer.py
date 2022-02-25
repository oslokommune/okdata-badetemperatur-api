import json
import base64
import logging
from decimal import DecimalException

from botocore.exceptions import ClientError

from badetemperatur_api.temperature_table import TemperatureTable


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_event(event, context):
    temperature_table = TemperatureTable()

    try:
        list(
            map(
                temperature_table.put_item,
                map(
                    TemperatureTable.to_dynamodb_format,
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


def b64_to_obj(b64):
    s = base64.b64decode(b64)
    obj = json.loads(s)
    logger.info(f"Received data: {obj}")
    return obj
