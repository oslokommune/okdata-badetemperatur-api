import unittest
import boto3
import src.main.temperature_reader as temperature_reader
import src.test.test_data.temperature_reader_test_data as test_data

from moto import mock_dynamodb2

def create_table(table_name, item_list):
    client = boto3.client('dynamodb', region_name='eu-west-1')
    client.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': 'locationId', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    sensor_data_table = dynamodb.Table(table_name)
    for item in item_list:
        sensor_data_table.put_item(Item=item)


class Tester(unittest.TestCase):

    @mock_dynamodb2
    def test_get_all_temperatures(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name, [test_data.item_1, test_data.item_2])

        response = temperature_reader.get_all_temperatures(test_data.http_event_no_path_params, None)
        self.assertDictEqual(response, test_data.get_all_temperatures_ok_response)

    @mock_dynamodb2
    def test_get_temperature(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name, [test_data.item_1, test_data.item_2])

        response = temperature_reader.get_temperature(test_data.http_event_with_path_params, None)
        self.assertDictEqual(response, test_data.get_temperature_ok_response)


    @mock_dynamodb2
    def test_query_for_item(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name, [test_data.item_1, test_data.item_2])

        item = temperature_reader.query_for_item(test_data.item_1['locationId'])
        self.assertDictEqual(item, test_data.item_1)

    @mock_dynamodb2
    def test_scan_for_items(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name, [test_data.item_1, test_data.item_2])

        items_in_table = temperature_reader.scan_for_items()
        self.assertListEqual(items_in_table, [test_data.item_1, test_data.item_2])


    def test_decimal_to_float(self):
        transformed_item = temperature_reader.from_dynamodb_format(test_data.item_1)
        self.assertDictEqual(transformed_item, test_data.item_1_transformed)


if __name__ == '__main__':
    unittest.main()