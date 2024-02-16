from decimal import Decimal

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('TestTableForMotoIssue')

table.put_item(Item={'id': 'foo', 'amount': Decimal(100)})
table.update_item(
    Key={'id': 'foo'},
    UpdateExpression='ADD amount :delta',
    ExpressionAttributeValues={':delta': -Decimal('88.3')},
)

assert Decimal(100) - Decimal('88.3') == Decimal('11.7')

items = table.scan()['Items']
assert items == [{'id': 'foo', 'amount': Decimal('11.7')}]

print(items)
