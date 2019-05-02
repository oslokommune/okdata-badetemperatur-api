import unittest
import boto3
import src.main.sensor_data_writer as sensor_data_writer
import src.test.test_data.sensor_data_writer_test_data as test_data

from moto import mock_dynamodb2

def create_table(table_name):
    client = boto3.client('dynamodb', region_name='eu-west-1')
    client.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': 'locationId', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )


def dynamodb_table(table_name):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    return dynamodb.Table(table_name)

class Tester(unittest.TestCase):

    @mock_dynamodb2
    def test_handle_event(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name)
        sensor_data_table = dynamodb_table(table_name)

        sensor_data_writer.handle_event(test_data.kinesis_event, None)

        items = sensor_data_table.scan()
        assert test_data.item_1 and test_data.item_2 in items['Items']


    @mock_dynamodb2
    def test_put_item(self):
        table_name = 'badetemperatur-latest'
        create_table(table_name)
        sensor_data_table = dynamodb_table(table_name)

        sensor_data_writer.put_item(test_data.item_1)

        assert test_data.item_1 in sensor_data_table.scan()['Items']

    def test_to_dynamo_db_format(self):
        new_item = sensor_data_writer.to_dynamodb_format(test_data.event_data_1)
        self.assertEqual(
            new_item['locationId'],
            test_data.event_data_1['location']['id']
        )
        self.assertEqual(
            float(new_item['temperature']['value']),
            test_data.event_data_1['temperature']['value']
        )
        self.assertEqual(
            float(new_item['location']['longitude']),
            test_data.event_data_1['location']['longitude']
        )
        self.assertEqual(
            float(new_item['location']['latitude']),
            test_data.event_data_1['location']['latitude']
        )


    def test_b64_to_obj(self):
        self.assertDictEqual(
            sensor_data_writer.b64_to_obj(test_data.b64_encoded_obj),
            test_data.obj_decoded
        )

if __name__ == '__main__':
    unittest.main()