# class A:
#
#     number = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         A.number += 1
#
#     def area(self):
#         return self.x * self.y
#
#     @classmethod
#     def items_number(cls):
#         return cls.number
#
#     @staticmethod
#     def greetings():
#         return 'Hello'
#
#
#
# obj1 = A(1, 2)
# obj2 = A(2, 3)
#
# print(obj1.x, obj1.y)
# print(obj2.x, obj2.y)



# from datetime import datetime
#
# date = datetime.strptime('2017-01-26', '%Y-%m-%d')




# Product = id, name, price
# OrderItem = product, quantity
# BaseOrder = id, items, customer_name


import re
import uuid

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_str(cls, text):
        pattern = r'name=(\w+), price=([\d.]+)'
        name, price = re.search(pattern, text).groups()
        return cls(name, float(price))


    def __str__(self):
        return f'{self.name} - {self.price} EURO'

    def __repr__(self):
        return f'Product(name={self.name}, price={self.price})'


class OrderItem:
    def __init__(self, product: Product, quantity=1):
        self.product = product
        self.quantity = quantity

    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product} x {self.quantity} = {self.total():.2f} EURO'


class Order:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.items = []
        self.name = name


    def total(self):
        return sum(item.total() for item in self.items)


    def __str__(self):
        return f'{self.id}: {self.name}\n' + '\n'.join(map(str, self.items)) + '\n' + f'\nTotal: {self.total():.2f}'


class DeliveryOrder(Order):

    def __init__(self, name: str, delivery_address: str):
        super().__init__(name=name)
        self.delivery_address = delivery_address


class PickupOrder(Order):
    def __init__(self, name: str):
        super().__init__(name)
        self.discount = 0.1


    def total(self):
        return super().total() * (1 - self.discount)


def order_factory(order_type: str, name, address: str=None) -> Order:
    if order_type == '1':
        return DeliveryOrder(name, address)
    if order_type == '2':
        return PickupOrder(name)
    return Order(name)



products = []

with open('products.txt', 'r') as f:
    for line in f:
        name, price = line.split(';')
        products.append(Product(name.strip(), price.strip()))


with open('products_dev.txt', 'r') as f:
    for line in f:
        products.append(Product.from_str(line))

for item in products:
    print(item)


print(products, sep='\n')



pr1 = Product('banana', 1)
pr2 = Product('apple', 2)
pr3 = Product('orange', 3)
pr4 = Product('kiwi', 4)


ans = input('Order Type? (1 - delivery, 2 - pickup, 3 - general) : ').strip().lower()
name = input('What is your name? ').strip()
address = None
if ans == '1':
    address = input('What is your delivery address? ').strip()


order_1 = order_factory(ans, name, address)

print(isinstance(order_1, Order))


order_item_1 = OrderItem(pr1, 2)
order_item_2 = OrderItem(pr2, 3)
order_item_3 = OrderItem(pr3, 4)

order_1.items.append(order_item_1)
order_1.items.append(order_item_2)
order_1.items.append(order_item_3)

print(order_1)
