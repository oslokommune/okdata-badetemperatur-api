import unittest

from moto import mock_dynamodb2

import badetemperatur_api.sensor_data_writer as sensor_data_writer
import test.test_data.sensor_data_writer_test_data as test_data
from test.test_utils import create_table


class Tester(unittest.TestCase):
    @mock_dynamodb2
    def test_handle_event(self):
        table_name = "badetemperatur-latest"
        sensor_data_table = create_table(table_name)

        sensor_data_writer.handle_event(test_data.kinesis_event, None)

        items = sensor_data_table.scan()

        assert test_data.item_1_sensor in items["Items"]
        assert test_data.item_2_sensor in items["Items"]
        assert test_data.item_1_manual in items["Items"]
        assert test_data.item_2_manual in items["Items"]

    def test_b64_to_obj(self):
        self.assertDictEqual(
            sensor_data_writer.b64_to_obj(test_data.b64_encoded_obj),
            test_data.obj_decoded,
        )


if __name__ == "__main__":
    unittest.main()
