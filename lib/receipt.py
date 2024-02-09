class Receipt():
    def __init__(self):
        pass
    
    def calculate_grand_total(self, order):
        total = 0
        for dish in order.order_list:
            total += float(dish.price)
        return total


    def format_receipt(self, order):
        formatted_receipt = f"""\n"""
        for item in sorted(set(order.order_list), key=lambda item: item.name):
            counter = order.order_list.count(item)
            formatted_receipt += f'{counter} {item.name}: (£{item.price})...{"£{:,.2f}".format(counter * float(item.price))}\n'
        formatted_receipt += f'TOTAL: {"£{:,.2f}".format(Receipt.calculate_grand_total(self, order))}'
        return formatted_receipt