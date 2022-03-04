import unittest
from decimal import Decimal

from moto import mock_dynamodb2

import test.test_data.sensor_data_writer_test_data as writer_test_data
import test.test_data.temperature_reader_test_data as reader_test_data
from badetemperatur_api.temperature_table import TemperatureTable
from test.test_utils import create_table


class Tester(unittest.TestCase):
    @mock_dynamodb2
    def test_query_for_item(self):
        table_name = "badetemperatur-latest"
        create_table(table_name, reader_test_data.dynamo_db_items)
        temperature_table = TemperatureTable()

        item_list = temperature_table.query_for_item(reader_test_data.location_id_1)

        self.assertCountEqual(
            item_list, [reader_test_data.item_1_sensor, reader_test_data.item_1_manual]
        )

    @mock_dynamodb2
    def test_scan_for_items(self):
        table_name = "badetemperatur-latest"
        create_table(table_name, reader_test_data.dynamo_db_items)
        temperature_table = TemperatureTable()

        items_in_table = temperature_table.scan_for_items()
        self.assertCountEqual(
            items_in_table,
            [
                reader_test_data.item_1_sensor,
                reader_test_data.item_1_manual,
                reader_test_data.item_2_sensor,
                reader_test_data.item_2_manual,
            ],
        )

    @mock_dynamodb2
    def test_put_item(self):
        table_name = "badetemperatur-latest"
        sensor_data_table = create_table(table_name)
        temperature_table = TemperatureTable()

        temperature_table.put_item(writer_test_data.item_1_sensor)

        assert writer_test_data.item_1_sensor in sensor_data_table.scan()["Items"]

    def test_to_dynamo_db_format(self):
        new_item = TemperatureTable.to_dynamodb_format(
            writer_test_data.event_data_1_sensor
        )
        self.assertDictEqual(new_item, writer_test_data.item_1_sensor)

    def test_float_to_decimal(self):
        f1 = 4.9e-324
        f2 = 4.24597
        f3 = 4.24497

        self.assertEqual(
            TemperatureTable._float_to_decimal(f1, num_decimals=2), Decimal("0.00")
        )
        self.assertEqual(
            TemperatureTable._float_to_decimal(f2, num_decimals=2), Decimal("4.25")
        )
        self.assertEqual(
            TemperatureTable._float_to_decimal(f3, num_decimals=2), Decimal("4.24")
        )
        self.assertEqual(TemperatureTable._float_to_decimal(f3), Decimal("4.24497"))

    def test_decimal_to_float(self):
        transformed_item = TemperatureTable.from_dynamodb_format(
            reader_test_data.item_1_sensor
        )
        self.assertDictEqual(
            transformed_item, reader_test_data.item_1_sensor_transformed
        )
