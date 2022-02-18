import unittest
import json
import badetemperatur_api.temperature_reader as temperature_reader
import test.test_data.temperature_reader_test_data as test_data

from test.test_utils import create_table
from moto import mock_dynamodb2
from moto.core import patch_resource

dynamo_db_items = [
    test_data.item_1_sensor,
    test_data.item_1_manual,
    test_data.item_2_sensor,
    test_data.item_2_manual,
]


class Tester(unittest.TestCase):
    @mock_dynamodb2
    def test_get_all_temperatures(self):
        patch_resource(temperature_reader.dynamodb)
        table_name = "badetemperatur-latest"
        create_table(table_name, dynamo_db_items)

        response = temperature_reader.get_all_temperatures(
            test_data.http_event_no_location, None
        )
        response_body = json.loads(response["body"])
        self.assertCountEqual(
            response_body, test_data.get_all_temperatures_manual_only_body
        )

    @mock_dynamodb2
    def test_get_all_temperatures_with_source_filter(self):
        patch_resource(temperature_reader.dynamodb)
        table_name = "badetemperatur-latest"
        create_table(table_name, dynamo_db_items)

        response_all_sources = temperature_reader.get_all_temperatures(
            test_data.http_event_no_location_all_sources, None
        )
        response_sensor_only = temperature_reader.get_all_temperatures(
            test_data.http_event_no_location_sensor_only, None
        )
        response_manual_only = temperature_reader.get_all_temperatures(
            test_data.http_event_no_location_manual_only, None
        )
        response_invalid_sources = temperature_reader.get_all_temperatures(
            test_data.http_event_no_location_invalid_sources, None
        )

        response_all_sources_body = json.loads(response_all_sources["body"])
        response_sensor_only_body = json.loads(response_sensor_only["body"])
        response_manual_only_body = json.loads(response_manual_only["body"])

        self.assertCountEqual(
            response_all_sources_body, test_data.get_all_temperatures_response_body
        )
        self.assertCountEqual(
            response_sensor_only_body,
            test_data.get_all_temperatures_sensor_only_response_body,
        )
        self.assertCountEqual(
            response_manual_only_body, test_data.get_all_temperatures_manual_only_body
        )

        self.assertEqual(response_invalid_sources["statusCode"], 400)

    @mock_dynamodb2
    def test_get_temperature(self):
        patch_resource(temperature_reader.dynamodb)
        temperature_reader.data_sources_default = "manual,sensor"
        table_name = "badetemperatur-latest"
        create_table(table_name, dynamo_db_items)

        response = temperature_reader.get_all_temperatures(
            test_data.http_event_with_location, None
        )
        response_body = json.loads(response["body"])
        self.assertCountEqual(response_body, test_data.get_temperature_response_body)

    @mock_dynamodb2
    def test_query_for_item(self):
        patch_resource(temperature_reader.dynamodb)
        table_name = "badetemperatur-latest"
        create_table(table_name, dynamo_db_items)

        item_list = temperature_reader.query_for_item(test_data.location_id_1)
        self.assertCountEqual(
            item_list, [test_data.item_1_sensor, test_data.item_1_manual]
        )

    @mock_dynamodb2
    def test_scan_for_items(self):
        patch_resource(temperature_reader.dynamodb)
        table_name = "badetemperatur-latest"
        create_table(table_name, dynamo_db_items)

        items_in_table = temperature_reader.scan_for_items()
        self.assertCountEqual(
            items_in_table,
            [
                test_data.item_1_sensor,
                test_data.item_1_manual,
                test_data.item_2_sensor,
                test_data.item_2_manual,
            ],
        )

    def test_filter_source(self):

        assert not temperature_reader.filter_source(test_data.item_1_sensor, [])
        assert not temperature_reader.filter_source(test_data.item_1_manual, ["kake"])
        assert temperature_reader.filter_source(
            test_data.item_1_sensor, ["sensor", "manual"]
        )
        assert temperature_reader.filter_source(
            test_data.item_1_manual, ["sensor", "manual"]
        )
        assert temperature_reader.filter_source(test_data.item_1_sensor, ["sensor"])
        assert not temperature_reader.filter_source(test_data.item_1_manual, ["sensor"])
        assert not temperature_reader.filter_source(test_data.item_1_sensor, ["manual"])
        assert temperature_reader.filter_source(test_data.item_1_manual, ["manual"])

    def test_decimal_to_float(self):
        transformed_item = temperature_reader.from_dynamodb_format(
            test_data.item_1_sensor
        )
        self.assertDictEqual(transformed_item, test_data.item_1_sensor_transformed)


if __name__ == "__main__":
    unittest.main()
