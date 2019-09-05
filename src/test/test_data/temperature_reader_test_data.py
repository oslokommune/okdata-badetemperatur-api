from src.test.test_data.test_data_utils import dynamodb_item_data, temperature_data

location_id_1, location_id_2 = "8171", "8172"

manual_data_name = "Manuell måling"

item_1_sensor = dynamodb_item_data(location_id_1, "sensor")
item_1_sensor_transformed = temperature_data(location_id_1, "sensor")

item_1_manual = dynamodb_item_data(location_id_1, manual_data_name)
item_1_manual_transformed = temperature_data(location_id_1, manual_data_name)

item_2_sensor = dynamodb_item_data(location_id_2, "sensor")
item_2_sensor_transformed = temperature_data(location_id_2, "sensor")

item_2_manual = dynamodb_item_data(location_id_2, manual_data_name)
item_2_manual_transformed = temperature_data(location_id_2, manual_data_name)


http_event_no_location = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "headers": {},
    "queryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {},
    "body": None,
    "isBase64Encoded": False,
}

http_event_no_location_all_sources = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "headers": {},
    "queryStringParameters": {"sources": "manual,sensor"},
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {},
    "body": None,
    "isBase64Encoded": False,
}


http_event_no_location_manual_only = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "headers": {},
    "queryStringParameters": {"sources": "manual"},
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {},
    "body": None,
    "isBase64Encoded": False,
}

http_event_no_location_sensor_only = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "headers": {},
    "queryStringParameters": {"sources": "sensor"},
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {},
    "body": None,
    "isBase64Encoded": False,
}


http_event_no_location_invalid_sources = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "headers": {},
    "queryStringParameters": {"sources": "kake"},
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {},
    "body": None,
    "isBase64Encoded": False,
}


get_all_temperatures_response_body = [
    item_1_sensor_transformed,
    item_1_manual_transformed,
    item_2_sensor_transformed,
    item_2_manual_transformed,
]


get_all_temperatures_manual_only_body = [
    item_1_manual_transformed,
    item_2_manual_transformed,
]

get_all_temperatures_sensor_only_response_body = [
    item_1_sensor_transformed,
    item_2_sensor_transformed,
]


http_event_with_location = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "headers": {},
    "queryStringParameters": {"location": location_id_1},
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {},
    "body": None,
    "isBase64Encoded": False,
}

get_temperature_response_body = [item_1_manual_transformed, item_1_sensor_transformed]


get_temperature_manual_only_response_body = [item_1_manual_transformed]

get_temperature_sensor_only_response_body = [item_1_sensor_transformed]
