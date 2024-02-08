from lib.menu import Menu
from unittest.mock import Mock

# test that Menu can receive dishes (use mocks here)
def test_dishes_go_into_menu():
    menu = Menu()
    mock_dish1 = Mock(name= 'dish1')
    mock_dish2 = Mock(name= 'dish2')
    menu.add_dish_to_menu(mock_dish1)
    menu.add_dish_to_menu(mock_dish2)
    assert menu.menu_list == [mock_dish1, mock_dish2]

# test that the menu can be formatted for the user to read
def test_menu_formatting():
    menu = Menu()
    mock_dish1 = Mock(name= 'dish1')
    mock_dish1.name = 'Boyish Cake Ramen'
    mock_dish1.price = '2.50'
    mock_dish2 = Mock(name= 'dish2')
    mock_dish2.name = 'Matching Cheesecake'
    mock_dish2.price = '3.50'
    menu.add_dish_to_menu(mock_dish1)
    menu.add_dish_to_menu(mock_dish2)
    assert menu.format_menu() == """
- Boyish Cake Ramen: £2.50
- Matching Cheesecake: £3.50
"""