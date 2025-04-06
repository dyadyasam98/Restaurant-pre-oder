from datetime import datetime, date, time
class Menu:
    def __init__(self, item_id, name, price, description, avaliable):
        self.item_id = item_id
        self.name = name
        self.price = self._validate_price(price)
        self.description = description
        self.avaliable = avaliable
    def _validate_price(self, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        return price
    def __str__(self):
        return f'{self.name} - {self.price} руб.'

class Table:
    def __init__(self, table_number, seats, is_booked=False):  # Переименовано из if_booked
       self.table_number = table_number
       self.seats = self._validate_seats(seats)  # Добавлена валидация
       self.is_booked = is_booked

    def book(self):
        if self.is_booked == False:
            self.is_booked = True
            return True
        return False
    def _validate_seats(self, seats):
        """Проверка, что количество мест - положительное число"""
        seats = int(seats)
        if seats <= 0:
            raise ValueError("Количество мест должно быть положительным числом")
        return seats
    def release(self):
       """Освобождает стол"""
       previous_status = self.is_booked
       self.is_booked = False
       return previous_status

class Order:
    def __init__(self, table, time, tel_number, customer_name, items):
        self.table = table
        self.time = time
        self.tel_number = tel_number
        self.customer_name = customer_name
        self.items = []
        self.created_add = datetime.now()
    def add_item(self, item_to_add, add_quantity = 1):
        for item in self.items:
            if item.menu_item.item_id == item_to_add.item_id:
                item.quantity += add_quantity
                return item
        order_item = OrderItem(item, add_quantity)
        self.items.append(order_item)
        return order_item
    def delete_item(self, item_to_del):
        for i, item in enumerate(self.items):
           if item.menu_item.item_id == item_to_del.item_id:
               return self.items.pop(i)
        return None
        
    def get_total(self):
        s = 0
        for order_item in self.items:
            s += order_item.get_subbtotal()
        return s
    def __str__(self):
        order_str = f"Заказ для стола №{self.table.table_number}\n"
        for item in self.items:
            order_str += f"- {item}\n"
        order_str += f"Итого: {self.get_total()} руб."
        return order_str


    
        
class OrderItem:
    def __init__(self, menu_item, quantity = 1):
        self.menu_item = menu_item
        self.quantity = quantity
    def get_subbtotal(self):
        return self.quantity * self.menu_item.price
    def __str__(self):
        return f'{self.menu_item.name} x {self.quantity} = {self.get_subbtotal()} руб.'
    
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = []
        self.menu = []
        self.orders = []

    def add_table(self, table):
        for t in self.tabels:
            if t.table_number == table.table_number:
                raise ValueError (f"Стол с номером {table.table_number} уже существует.")
        self.tables.append(table)
        return table.table_number

    def add_menu_item(self, menu_item):
        for i in self.menu:
            if i.item_id == menu_item.item_id:
                raise ValueError (f'Блюдо с ID {menu_item.item_id} уже существет ({i.name}).')
        self.menu.append(menu_item)
    
    def get_dish_by_id(self, id):
        for d in self.menu:
            if d.item_id == id:
                return d
        return None
    
    def get_dish_by_name(self, name):
        for d in self.menu:
            if d.name.lower() == name:
                return d
        return None
    
    def get_available_tables(self):
        return [table for table in self.tables if table.is_booked == False]

    def get_table_by_number(self, number):
        for t in self.tables:
            if t.table_number == number:
                return t
        return None
    
    def get_dish_with_id(self, id):
        for d in self.menu:
            if d.item_id == id:
                return d
        return None
    
    def get_dish_with_name(self, name):
        for d in self.menu:
            if d.name == name:
                return d
        return None

    def book_table(self, user_name, user_number, n_table, time):
        table_to_book = self.get_table_by_number(n_table)
        if not table_to_book or not table_to_book.book():
            return None
        new_order = Order(table_to_book, time, user_number, user_name)
        self.orders.append(new_order)
        return new_order

    def release(self, n_table):
        table_to_release = self.get_table_by_number()
        if table_to_release:
            table_to_release.release()
        return False

        
        

    def place_order(self, n_table, menu_items):
        table_to_order = 0
        for order in self.orders:
            if order.table.table_number == n_table:
                for item in menu_items:
                    order.items.append(item)
                return order
        return None
    
    def get_order_by_table(self, id):
        for order in self.orders:
            if order.table.table_number == id:
                return order
        return None

    def add_menu_item(self, dish):
        for d in self.menu:
            if d.item_id == dish.item_id:
                raise ValueError(f"Блюдо с ID {d.item_id} уже существует в меню")
        self.menu.append(dish)
      

