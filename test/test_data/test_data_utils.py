from decimal import Decimal


def dynamodb_item_data(location_id, name):
    return {
        "locationId": location_id,
        "location": {
            "id": location_id,
            "name": "Location Name",
            "latitude": Decimal("59.89390"),
            "longitude": Decimal("10.72674"),
        },
        "name": name,
        "temperature": {"value": Decimal("4.34"), "unit": "C"},
        "measureTime": "2019-02-19T12:43:09.000+0000",
    }


def temperature_data(location_id, name):
    return {
        "location": {
            "id": location_id,
            "name": "Location Name",
            "latitude": 59.89390,
            "longitude": 10.72674,
        },
        "name": name,
        "temperature": {"value": 4.34, "unit": "C"},
        "measureTime": "2019-02-19T12:43:09.000+0000",
    }
