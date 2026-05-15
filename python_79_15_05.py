from dataclasses import dataclass
from abc import ABC, abstractmethod


class PaymentTypeError(Exception):
    pass


@dataclass
class OrderItem:
    name: str
    price: int | float
    quantity: int | float = 0

    def __setattr__(self, key, value):
        if key in ('price', 'quantity'):
            if not isinstance(value, int | float):
                raise TypeError(f'{key} can only accept int or float')
            if value <= 0:
                raise ValueError(f'{key} can only accept positive numbers')

        super().__setattr__(key, value)


# class OrderItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if not isinstance(value, float | int):
#             raise TypeError('Price must be float or int')
#
#         if value <= 0:
#             raise ValueError('Price must be greater than 0')
#
#         self.__price = value
#
#     @property
#     def quantity(self):
#         return self.__quantity
#
#     @quantity.setter
#     def quantity(self, value):
#         if not isinstance(value, float | int):
#             raise TypeError('Quantity must be float or int')
#
#         if value <= 0:
#             raise ValueError('Quantity must be greater than 0')
#
#         self.__quantity = value


class Order:
    def __init__(self):
        self.__items = []

        self.status = False


    def add_item(self, item):
        self.__items.append(item)

    def total(self):
        return sum(item.price * item.quantity for item in self.__items)

    def __iter__(self):
        return iter(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return '\n'.join(map(str, self))


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class DebitPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = True


class CreditPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = True


class PayPalPayment(PaymentProcessor):
    def __init__(self, email):
        self.email = email
    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying email: {self.email}")
        order.status = True


x1 = OrderItem('Apple', 10, 1)
x2 = OrderItem('Banana', 5, 2)
x3 = OrderItem('Orange', 5, 3)

order = Order()
order.add_item(x1)
order.add_item(x2)
order.add_item(x3)
for item in order:
    print(item)

print(order[2])

print(len(order))

print(order)


print(order.status)
PayPalPayment('2345678').pay(order)
print(order.status)