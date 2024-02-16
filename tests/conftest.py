import boto3
import pytest
from moto import mock_aws


@mock_aws
@pytest.fixture
def tables():
    with mock_aws():
        dynamodb = boto3.resource('dynamodb')

        class Tables:
            table = dynamodb.create_table(
                TableName='TestTableForMotoIssue',
                AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
                KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
                BillingMode='PAY_PER_REQUEST',
            )

        yield Tables()
