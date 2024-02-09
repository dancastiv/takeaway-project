from lib.receipt import Receipt
from unittest.mock import Mock, MagicMock

# test that grand total can be calculated
def test_calculate_grand_total():
    receipt = Receipt()
    mock_takeout_order = Mock()
    mock_dish1 = Mock(name= 'dish1')
    mock_dish1.name = 'Boyish Cake Ramen'
    mock_dish1.price = '2.50'
    mock_dish2 = Mock(name= 'dish2')
    mock_dish2.name = 'Matching Cheesecake'
    mock_dish2.price = '3.50'
    mock_takeout_order.order_list = [mock_dish1, mock_dish2]
    assert receipt.calculate_grand_total(mock_takeout_order) == 6

# test that receipt is formatted correctly
def test_format_receipt():
    receipt = Receipt()
    mock_takeout_order = Mock()
    mock_dish1 = Mock(name= 'dish1')
    mock_dish1.name = 'Boyish Cake Ramen'
    mock_dish1.price = '2.50'
    mock_dish2 = Mock(name= 'dish2')
    mock_dish2.name = 'Matching Cheesecake'
    mock_dish2.price = '3.50'
    mock_takeout_order.order_list = [mock_dish1, mock_dish2]
    assert receipt.format_receipt(mock_takeout_order) == """
1 Boyish Cake Ramen: (£2.50)...£2.50
1 Matching Cheesecake: (£3.50)...£3.50
TOTAL: £6.00"""

# test that formatting still works if user orders more than one of a dish
def test_format_receipt():
    receipt = Receipt()
    mock_takeout_order = Mock()
    mock_dish1 = Mock(name= 'dish1')
    mock_dish1.name = 'Boyish Cake Ramen'
    mock_dish1.price = '2.50'
    mock_dish2 = Mock(name= 'dish2')
    mock_dish2.name = 'Matching Cheesecake'
    mock_dish2.price = '3.50'
    mock_dish3 = Mock(name='dish3')
    mock_dish3.name = 'Wack-a-mole'
    mock_dish3.price = '0.69'
    mock_takeout_order.order_list = [mock_dish1, mock_dish2, mock_dish3, mock_dish2]
    assert receipt.format_receipt(mock_takeout_order) == """
1 Boyish Cake Ramen: (£2.50)...£2.50
2 Matching Cheesecake: (£3.50)...£7.00
1 Wack-a-mole: (£0.69)...£0.69
TOTAL: £10.19"""