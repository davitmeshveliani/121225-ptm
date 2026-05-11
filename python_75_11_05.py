# class Product:
#     TAX_RATE = 0.2
#     def __init__(self, name, price):
#         self.name = name
#         self.set_price(price)
#
#     def get_price(self):
#         return self.__price * (1 + self.TAX_RATE)
#
#     def set_price(self, value):
#         if not isinstance(value, float | int):
#             raise TypeError('value must be float or int')
#         if value <= 0:
#             raise ValueError('value must be positive')
#
#         self.__price = value
#
#     def __str__(self):
#         return f'{self.name}: {self.get_price()}'
#
#
# x = Product('Banana', 100)
# print(x.get_price())
# print(x)
#
#
# x.set_price(1000)
# print(x.get_price())
import hashlib


#
# class Product:
#     TAX_RATE = 0.2
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     @property
#     def price(self):
#         return self.__price * (1 + self.TAX_RATE)
#
#     @price.setter
#     def price(self, value):
#         if not isinstance(value, float | int):
#             raise TypeError('value must be float or int')
#         if value <= 0:
#             raise ValueError('value must be positive')
#
#         self.__price = value
#
#
#     @price.deleter
#     def price(self):
#         pass
#
#     def __str__(self):
#         return f'{self.name}: {self.price}'
#
#
# x = Product('Banana', 100)
# print(x.price)
# print(x)
#
#
# x.price = 1000
# print(x.price)
#
# print(Product.__dict__)



# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @x.setter
#     def x(self, x):
#         if not isinstance(x, int):
#             raise TypeError('x must be an integer')
#         self.__x = x
#
#     @y.setter
#     def y(self, y):
#         if not isinstance(y, int):
#             raise TypeError('y must be an integer')
#         self.__y = y
#
#
#     def __str__(self):
#         return f'Point({self.x}, {self.y})'
#
#     @staticmethod
#     def distance(x1, x2):
#         return ((x1.x - x2.x) ** 2 + (x1.y - x2.y) ** 2) ** 0.5
#
#
# p1 = Point(1, 2)
# print(p1)
# p2 = Point(2, 3)
# print(p2)
#
#
# print(Point.distance(p1, p2))


# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __setattr__(self, name, value):
#         if name in ('x', 'y'):
#             if not isinstance(value, int):
#                 raise TypeError(f'{name} must be an integer')
#
#             super().__setattr__(f'_Point__{name}', value)
#
#
#     @property
#     def x(self):
#         return self.__x
#
#     @property
#     def y(self):
#         return self.__y
#
#
#     def __str__(self):
#         return f'Point({self.x}, {self.y})'
#
#     @staticmethod
#     def distance(x1, x2):
#         return ((x1.x - x2.x) ** 2 + (x1.y - x2.y) ** 2) ** 0.5
#
#
# p1 = Point(1, 2)
# print(p1)
# p2 = Point(2, 3)
# print(p2)
#
# print(p1.__dict__)
#
# print(Point.distance(p1, p2))
#



# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __setattr__(self, name, value):
#         if name in ('x', 'y'):
#             if not isinstance(value, int):
#                 raise TypeError(f'{name} must be an integer')
#
#             super().__setattr__(f'_Point__{name}', value)
#
#     def __getattribute__(self, item):
#         if item in ('x', 'y'):
#             return super().__getattribute__(f'_Point__{item}')
#         return super().__getattribute__(item)
#
#     def __str__(self):
#         return f'Point({self.x}, {self.y})'
#
#     @staticmethod
#     def distance(x1, x2):
#         return ((x1.x - x2.x) ** 2 + (x1.y - x2.y) ** 2) ** 0.5
#
#
# p1 = Point(1, 2)
# print(p1)
# p2 = Point(2, 3)
# print(p2)
#
# print(p1.__dict__)
#
# print(Point.distance(p1, p2))
#
#

class User:
    USERNAME_LENGTH = 5
    count = 0

    def __new__(cls, *args, **kwargs):
        user = super().__new__(cls)
        
        return user

    def __init__(self, username, password):
        self.username = username
        self.password = password

        User.count += 1 # 3

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return hashlib.md5(self.__password.encode('utf-8')).hexdigest()

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('password must be a string')

        self.__password = value


    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError('username must be a string')

        username = value.strip()
        if not username:
            raise ValueError('username cannot be empty')
        if len(username) < User.USERNAME_LENGTH:
            raise ValueError(f'username must be at least {User.USERNAME_LENGTH} characters long')

        self.__username = username



u1 = User('user1', 'password')
u2 = User('user2', 'password')
print(u1.username, u1.password)
print(u2.username, u2.password)

