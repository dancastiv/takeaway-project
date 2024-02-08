class Menu():
    def __init__(self):
        self.menu_list = []

    def add_dish_to_menu(self, dish):
        self.menu_list.append(dish)

    def format_menu(self):
        formatted_menu = f"""\n"""
        for item in self.menu_list:
            formatted_menu += f'- {item.name}: £{item.price}\n'
        return formatted_menu
