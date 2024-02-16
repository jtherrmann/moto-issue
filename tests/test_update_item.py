from decimal import Decimal


def test_update_item_bad(tables):
    tables.table.put_item(Item={'id': 'foo', 'amount': Decimal(100)})
    tables.table.update_item(
        Key={'id': 'foo'},
        UpdateExpression='ADD amount :delta',
        ExpressionAttributeValues={':delta': -Decimal('88.3')},
    )
    assert Decimal(100) - Decimal('88.3') == Decimal('11.7')
    assert tables.table.scan()['Items'] == [{'id': 'foo', 'amount': Decimal('11.7')}]


def test_update_item_good(tables):
    tables.table.put_item(Item={'id': 'foo', 'amount': Decimal(100)})
    tables.table.update_item(
        Key={'id': 'foo'},
        UpdateExpression='ADD amount :delta',
        ExpressionAttributeValues={':delta': -Decimal('0.3')},
    )
    assert Decimal(100) - Decimal('0.3') == Decimal('99.7')
    assert tables.table.scan()['Items'] == [{'id': 'foo', 'amount': Decimal('99.7')}]
