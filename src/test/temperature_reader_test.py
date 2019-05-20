import unittest
import json
import src.main.temperature_reader as temperature_reader
import src.test.test_data.temperature_reader_test_data as test_data

from src.test.test_utils import create_table
from moto import mock_dynamodb2

class Tester(unittest.TestCase):

    @mock_dynamodb2
    def test_get_all_temperatures(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name, [
            test_data.item_1_sensor,
            test_data.item_1_manual,
            test_data.item_2_sensor,
            test_data.item_2_manual
        ])

        response = temperature_reader.get_all_temperatures(test_data.http_event_no_path_params, None)
        response_body = json.loads(response['body'])
        self.assertCountEqual(response_body, test_data.get_all_temperatures_response_body)
    @mock_dynamodb2
    def test_get_temperature(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name, [
            test_data.item_1_sensor,
            test_data.item_1_manual,
            test_data.item_2_sensor,
            test_data.item_2_manual
        ])

        response = temperature_reader.get_temperature(test_data.http_event_with_path_params, None)
        response_body = json.loads(response['body'])
        self.assertCountEqual(response_body, test_data.get_temperature_response_body)


    @mock_dynamodb2
    def test_query_for_item(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name, [
            test_data.item_1_sensor,
            test_data.item_1_manual,
            test_data.item_2_sensor,
            test_data.item_2_manual
        ])

        item_list = temperature_reader.query_for_item(test_data.location_id_1)
        self.assertCountEqual(
            item_list,
            [test_data.item_1_sensor, test_data.item_1_manual]
        )

    @mock_dynamodb2
    def test_scan_for_items(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name, [
            test_data.item_1_sensor,
            test_data.item_1_manual,
            test_data.item_2_sensor,
            test_data.item_2_manual
        ])

        items_in_table = temperature_reader.scan_for_items()
        self.assertCountEqual(
            items_in_table,
            [test_data.item_1_sensor,
             test_data.item_1_manual,
             test_data.item_2_sensor,
             test_data.item_2_manual])


    def test_decimal_to_float(self):
        transformed_item = temperature_reader.from_dynamodb_format(test_data.item_1_sensor)
        self.assertDictEqual(transformed_item, test_data.item_1_sensor_transformed)


if __name__ == '__main__':
    unittest.main()