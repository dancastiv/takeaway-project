class Receipt():
    def __init__(self):
        pass
    
    def calculate_grand_total(self, order):
        total = 0
        for dish in order.order_list:
            total += float(dish.price)
        return total


    def format_receipt(self, order):
        # parameters:
        #     order: list of dishes from TakoutOrder class
        # side effects:
        #     run #calculate_grand_total here
        # returns:
        #     formatted receipt
        pass