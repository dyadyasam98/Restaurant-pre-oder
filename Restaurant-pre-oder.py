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

class Order:
    def __init__(self, table, time):
        self.table = table
        self.time = time
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

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
                order = Order(table, time)
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

restaurant = Restaurant("Ресторан 1")
restaurant.add_table(Table(1, 2, False))
restaurant.add_table(Table(2, 4, False))
restaurant.add_menu_item(Menu(1, "Паста", 200))
restaurant.add_menu_item(Menu(2, "Пицца", 300))

print("Добро пожаловать в ресторан!")

# Получаем свободные столы
available_tables = restaurant.get_available_tables()
print("Доступные столы:")
for table in available_tables:
    print(f"Стол №{table.table_number}, Мест: {table.seats}")

# Запрос данных у юзера
table_number = int(input("Введите номер стола, который хотите забронировать: "))
time = input("Введите время бронирования (например, 18:00): ")

# Оформление бронирования
order = restaurant.book_table(table_number, time)
# Если стол свободен, выводим меню
if order:
    print(f"Бронирование успешно: Стол №{order.table.table_number} в {order.time}")
    print("\nМеню:")
    for user_dish in restaurant.menu:
        print(f"{user_dish.name} ({user_dish.price} руб.)")

    # Формируем заказ
    selected_items = []
    while True:
        dish_name = input("Введите название блюда для предзаказа (или 'завершить' для завершения): ")
        if dish_name.lower() == 'завершить':
            break

        # ищем блюдо
        user_dish = 0
        for item in restaurant.menu:
            if item.name.lower() == dish_name.lower():
                user_dish = item
                break
        # Если нашли блюдо
        if user_dish:
            selected_items.append(user_dish)
        # Если не нашли
        else:
            print("Такого блюда нет в меню!")

    # Размещаем заказ на кухню
    restaurant.place_order(table_number, selected_items)
    print("Ваш заказ сделан!")

    # Вывод информации о заказе
    print("\nИнформация о вашем заказе:")
    print(f"Стол: №{order.table.table_number}, Время: {order.time}")

    # Подсчет количества блюд и общей суммы
    order_summary = []
    total_price = 0

    for item in order.items:
        dish_status = False
        for summary_item in order_summary:
            # Если блюдо уже есть, то увеличиваем количество
            if summary_item['name'] == item.name:
                summary_item['quantity'] += 1
                dish_status = True
                break
        # Если не нашли блюдо в заказе, то создаем новое с количесвтом 1
        if dish_status == False:
            order_summary.append({'name': item.name, 'quantity': 1, 'price': item.price})

        total_price += item.price
    # Выводим заказ для юзера
    print("Ваш заказ:")
    for summary_item in order_summary:
        print(f"- {summary_item['name']} ({summary_item['price']} руб.) x {summary_item['quantity']} шт.")

    print(f"Общая сумма: {total_price} руб.")
# Если стол уже забронирован
else:
    print("Не удалось забронировать стол. Проверьте наличие свободных столов.")