import unittest
import boto3
import src.main.temperature_reader as temperature_reader
import src.test.test_data.temperature_reader_test_data as test_data

from moto import mock_dynamodb2

def create_table(table_name, item_list):
    client = boto3.client('dynamodb', region_name='eu-west-1')
    client.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': 'deviceId', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'deviceId', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    temperature_table = dynamodb.Table(table_name)

    for item in item_list:
        temperature_table.put_item(Item=item)


class Tester(unittest.TestCase):

    @mock_dynamodb2
    def test_get_all_temperatures(self):
        table_name = 'badeball-latest'
        create_table(table_name, [test_data.item_1, test_data.item_2])

        response = temperature_reader.get_all_temperatures(test_data.get_all_temperatures_http_event, None)
        self.assertDictEqual(response, test_data.get_all_temperatures_ok_response)

    @mock_dynamodb2
    def test_scan_for_items(self):
        table_name = 'badeball-latest'
        create_table(table_name, [test_data.item_1, test_data.item_2])

        items_in_table = temperature_reader.scan_for_items()
        self.assertListEqual(items_in_table, [test_data.item_1, test_data.item_2])


    def test_transform_item(self):
        transformed_item = temperature_reader.transform_item(test_data.item_1)
        self.assertDictEqual(transformed_item, test_data.item_1_transformed)

    def test_extract_temperature(self):
        temperature = temperature_reader.extract_temperature(test_data.item_1['sensors'])
        self.assertEqual(temperature, 22.675046226232894)

if __name__ == '__main__':
    unittest.main()