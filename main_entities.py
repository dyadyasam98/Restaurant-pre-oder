class Menu:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Table:
    def __init__(self, table_number, seats, if_booked):
        self.table_number = table_number
        self.seats = seats
        self.if_booked = if_booked

    def book(self):
        if self.if_booked == False:
            self.if_booked = True
            return True
        return False

class Book:
    def __init__(self, table, time):
        self.table = table
        self.time = time
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
        
class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = []
        self.menu = []
        self.orders = []

    def add_table(self, table):
        self.tables.append(table)

    def add_menu_item(self, menu_item):
        self.menu.append(menu_item)

    def get_available_tables(self):
        available_tables = []
        for table in self.tables:
            if table.if_booked == False:
                available_tables.append(table)
        return available_tables

    def book_table(self, table_number, time):
        for table in self.tables:
            if table.table_number == table_number and table.book() == True:
                order = Book(table, time)
                self.orders.append(order)
                return order
        return None

    def place_order(self, table_number, menu_items):
        for order in self.orders:
            if order.table.table_number == table_number:
                for item in menu_items:
                    order.add_item(item)
                return order
        return None