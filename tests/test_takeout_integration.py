from lib.takeout_order import TakeoutOrder
from lib.dish import Dish
from lib.menu import Menu
from lib.receipt import Receipt
import pytest

# test that before a user can even order, dishes can be added to the menu and it is displayed properly
def test_menu_formatting():
    menu = Menu()
    dish1 = Dish('Boshu Kakuni Ramen', '5.60')
    dish2 = Dish('Matcha Cheesecake', '4.50')
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    menu.menu_list == [dish1, dish2]
    assert menu.format_menu() == """
- Boshu Kakuni Ramen: £5.60
- Matcha Cheesecake: £4.50
"""

# test that user can add dishes from menu to their order
def  test_add_dishes_to_order():
    takeout_order = TakeoutOrder()
    dish1 = Dish('Boshu Kakuni Ramen', '5.60')
    dish2 = Dish('Matcha Cheesecake', '4.50')
    takeout_order.add_dish(dish1, 1)
    takeout_order.add_dish(dish2, 1)
    assert takeout_order.order_list == [dish1, dish2]

# test that user can add multiple of a dish to their order
def test_add_more_than_single_of_a_dish():
    takeout_order = TakeoutOrder()
    dish1 = Dish('Boshu Kakuni Ramen', '5.60')
    dish2 = Dish('Matcha Cheesecake', '4.50')
    dish3 = Dish('Guacamole', '0.99')
    takeout_order.add_dish(dish1, 1)
    takeout_order.add_dish(dish3, 3)
    takeout_order.add_dish(dish2, 1)
    assert takeout_order.order_list == [dish1, dish3, dish3, dish3, dish2]

# test that a user can ask to see the full menu and it'll be shown to them in a formatted presentation
def test_user_can_read_menu():
    menu = Menu()
    takeout_order = TakeoutOrder()
    dish1 = Dish('Boshu Kakuni Ramen', '5.60')
    dish2 = Dish('Matcha Cheesecake', '4.50')
    dish3 = Dish('Guacamole', '0.99')
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    menu.add_dish_to_menu(dish3)
    assert takeout_order.see_menu(menu) == """
- Boshu Kakuni Ramen: £5.60
- Matcha Cheesecake: £4.50
- Guacamole: £0.99
"""

# test that user can see itemised receipt with grand total
def test_see_receipt():
    menu = Menu()
    takeout_order = TakeoutOrder()
    receipt = Receipt()
    dish1 = Dish('Boshu Kakuni Ramen', '5.60')
    dish2 = Dish('Matcha Cheesecake', '4.50')
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    takeout_order.add_dish(dish1, 1)
    takeout_order.add_dish(dish2, 1)
    assert takeout_order.see_receipt(receipt) == """
1 Boshu Kakuni Ramen: (£5.60)...£5.60
1 Matcha Cheesecake: (£4.50)...£4.50
TOTAL: £10.10"""

# test that user can see itemised receipt with grand total when ordering multiple of a dish
def test_see_receipt_with_more_items():
    menu = Menu()
    takeout_order = TakeoutOrder()
    receipt = Receipt()
    dish1 = Dish('Boshu Kakuni Ramen', '5.60')
    dish2 = Dish('Matcha Cheesecake', '4.50')
    dish3 = Dish('Guacamole', '0.99')
    takeout_order.add_dish(dish1, 1)
    takeout_order.add_dish(dish2, 1)
    takeout_order.add_dish(dish3, 2)
    takeout_order.add_dish(dish2, 1)
    assert takeout_order.see_receipt(receipt) == """
1 Boshu Kakuni Ramen: (£5.60)...£5.60
2 Guacamole: (£0.99)...£1.98
2 Matcha Cheesecake: (£4.50)...£9.00
TOTAL: £16.58"""