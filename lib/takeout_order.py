class TakeoutOrder:
    def __init__(self):
        self.order_list = []

    def add_dish(self, dish, amount):
        while amount > 0:
            self.order_list.append(dish)
            amount -= 1

    def see_menu(self, menu):
        return menu.format_menu()
    
    def see_receipt(self, receipt):
        # returns instance of Receipt class (formatted to show dishes and prices + grand total)
        return receipt.format_receipt()

        # formatted_menu = f"""\n"""
        # for item in self.menu_list:
        #     formatted_menu += f'- {item.name}: £{item.price}\n'
        # return formatted_menu