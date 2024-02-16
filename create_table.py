import boto3

dynamodb = boto3.resource('dynamodb')

dynamodb.create_table(
    TableName='TestTableForMotoIssue',
    AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
    KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
    BillingMode='PAY_PER_REQUEST',
)
