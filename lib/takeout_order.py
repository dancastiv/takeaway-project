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
        return receipt.format_receipt(self)
