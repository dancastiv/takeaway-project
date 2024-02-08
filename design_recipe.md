# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

bonus:
As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
it's on paper lol

```

_Also design the interface of each class in more detail._

```python

class TakeoutOrder:
    def __init__(self):
        # Side effect: initialise order list
        pass

    def add_dish(self, dish, amount):
        # parameters:
        #   dish: instance of Dish class (contains dish name and price)
        #   amount: int representing how many of that particular dish are to be ordered
        # returns nothing
        pass

    def see_menu(self):
        # returns: menu (in a formatted presentation?)
        pass
    
    def see_receipt(self):
        # returns instance of Receipt class (formatted to show dishes and prices + grand total)
        pass

class Menu():
    def __init__(self):
        # side effect: initialise list of dishes
        pass

    def add_dish_to_menu(self, dish)
        # parameters:
        #     dish: instance of Dish class
        # side effects:
        #     adds dish to list of dishes
        # returns nothing

    def format_menu(self):
        # returns formatted menu to show to user
        pass

class Dish():
    def __init__(self, name, price):
        # parameters:
        #     name of dish
        #     price
        # returns nothing
        pass

class Receipt():
    def __init__(self):
        pass
    
    def calculate_grand_total(self, order):
        # parameters:
        #     order: list of dishes from TakeoutOrder class
        # returns:
        #     grand total to be paid
        pass

    def format_receipt(self, order):
        # parameters:
        #     order: list of dishes from TakoutOrder class
        # side effects:
        #     run #calculate_grand_total here
        # returns:
        #     formatted receipt
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

# test that before a user can even order, dishes can be added to the menu and it is displayed properly
menu = Menu()
dish1 = Dish('Boshu Kakuni Ramen', '5.60')
dish2 = Dish('Matcha Cheesecake', '4.50')
menu.add(dish1)
menu.add(dish2)
menu.menu_list => [dish1, dish2]
menu.format_menu =>
""" 
- Boshu Kakuni Ramen: £5.60
- Matcha Cheesecake: £4.50
"""

# test that user can add dishes from menu to their order
menu = Menu()
takeout_order = TakeoutOrder()
dish1 = Dish('Boshu Kakuni Ramen', '5.60')
dish2 = Dish('Matcha Cheesecake', '4.50')
menu.add(dish1)
menu.add(dish2)
takeout_order.add_dish(dish1, 1)
takeout_order.add_dish(dish2, 1)
takeout_order.order_list => [dish1, dish2]

# test that user can see itemised receipt with grand total
menu = Menu()
takeout_order = TakeoutOrder()
dish1 = Dish('Boshu Kakuni Ramen', '5.60')
dish2 = Dish('Matcha Cheesecake', '4.50')
menu.add(dish1)
menu.add(dish2)
takeout_order.add_dish(dish1, 1)
takeout_order.add_dish(dish2, 1)
takeout_order.see_receipt() =>
"""
1 Boshu Kakuni Ramen (£5.60)...£5.60
1 Matcha Cheesecake: (£4.50)...£4.50
TOTAL: £10.10
"""




```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

# Dish Class
# test that the dish class can be utilised to create dishes 
dish = Dish('Boshu Kakuni Ramen', '5.60')
dish.name => 'Boshu Kakuni Ramen'
dish.price => '5.60'

# Menu Class
# test that Menu can receive dishes (use mocks here)
menu = Menu()
mock_dish1 = Mock()
mock_dish2 = Mock()
menu.add(mock_dish1)
menu.add(mock_dish2)
menu.menu_list => [mock_dish1, mock_dish2]

# test that menu formats properly (mocks here)

# TakoutOrder Class
# test that dishes can be added
# test that user can see receipt

# Receipt Class
# test that grand total can be calculated
# test that receipt is formatted correctly


```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
