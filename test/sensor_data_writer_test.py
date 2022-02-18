import unittest
import badetemperatur_api.sensor_data_writer as sensor_data_writer
import test.test_data.sensor_data_writer_test_data as test_data
from test.test_utils import create_table

from decimal import Decimal
from moto import mock_dynamodb2
from moto.core import patch_resource


class Tester(unittest.TestCase):
    @mock_dynamodb2
    def test_handle_event(self):
        patch_resource(sensor_data_writer.dynamodb)
        table_name = "badetemperatur-latest"
        sensor_data_table = create_table(table_name)

        sensor_data_writer.handle_event(test_data.kinesis_event, None)

        items = sensor_data_table.scan()

        assert test_data.item_1_sensor in items["Items"]
        assert test_data.item_2_sensor in items["Items"]
        assert test_data.item_1_manual in items["Items"]
        assert test_data.item_2_manual in items["Items"]

    @mock_dynamodb2
    def test_put_item(self):
        patch_resource(sensor_data_writer.dynamodb)
        table_name = "badetemperatur-latest"
        sensor_data_table = create_table(table_name)

        sensor_data_writer.put_item(test_data.item_1_sensor)

        assert test_data.item_1_sensor in sensor_data_table.scan()["Items"]

    def test_to_dynamo_db_format(self):
        new_item = sensor_data_writer.to_dynamodb_format(test_data.event_data_1_sensor)
        self.assertDictEqual(new_item, test_data.item_1_sensor)

    def test_b64_to_obj(self):
        self.assertDictEqual(
            sensor_data_writer.b64_to_obj(test_data.b64_encoded_obj),
            test_data.obj_decoded,
        )

    def test_float_to_decimal(self):
        f1 = 4.9e-324
        f2 = 4.24597
        f3 = 4.24497
        self.assertEqual(
            sensor_data_writer.float_to_decimal(f1, num_decimals=2), Decimal("0.00")
        )
        self.assertEqual(
            sensor_data_writer.float_to_decimal(f2, num_decimals=2), Decimal("4.25")
        )
        self.assertEqual(
            sensor_data_writer.float_to_decimal(f3, num_decimals=2), Decimal("4.24")
        )
        self.assertEqual(sensor_data_writer.float_to_decimal(f3), Decimal("4.24497"))


if __name__ == "__main__":
    unittest.main()
