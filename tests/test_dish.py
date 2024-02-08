from lib.dish import Dish

# test that the dish class can be utilised to create dishes 
def test_dishes_added_to_dish():
    dish = Dish('Boshu Kakuni Ramen', '5.60')
    assert dish.name == 'Boshu Kakuni Ramen'
    assert dish.price == '5.60'