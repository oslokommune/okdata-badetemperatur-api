import boto3


def create_table(table_name, item_list=[]):
    client = boto3.client('dynamodb', region_name='eu-west-1')
    client.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'locationId', 'KeyType': 'HASH'},
            {'AttributeName': 'name', 'KeyType': 'Range'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'locationId', 'AttributeType': 'S'},
            {'AttributeName': 'name', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )

    sensor_data_table = dynamodb_table(table_name)
    for item in item_list:
        sensor_data_table.put_item(Item=item)

    return sensor_data_table


def dynamodb_table(table_name):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    return dynamodb.Table(table_name)