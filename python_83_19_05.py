# # class A:
# #
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def __str__(self):
# #         return f'A from STR({self.x}, {self.y})'
# #
# #     def __repr__(self):
# #         return f'A from REPR({self.x}, {self.y})'
# #
# #
# #
# #
# # objects = [A(1, 2), A(2, 3), A(3, 4), A(4, 5)]
# #
# # for item in objects:
# #     # print(item)
# #     tmp = str(item)
# #     print(tmp)
# #
# # print(objects)
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __mul__(self, other):
#         if isinstance(other, int | float):
#             return Circle(self.radius * other)
#         return NotImplemented
#
#     def __str__(self):
#         return f"Circle with radius {self.radius}"
#
#     # Protocol Iterator
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         pass
#
#     # Protocol Sequence
#     def __getitem__(self, key):
#         pass
#
#     def __len__(self):
#         pass
#
#     # Descriptor Protocol
#     def __get__(self, instance, owner):
#         pass
#
#     def __set__(self, instance, value):
#         pass
#
#     def __delete__(self, instance):
#         pass
#
#     # Context Manager
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     # CallAble
#     def __call__(self, *args, **kwargs):
#         pass
#
#
#
# # with Circle(1) as circle:
# #     pass
#
#
# x1 = Circle(5)
# x2 = Circle(7)
#
# if x1 > x2: # x1.__gt__(x2)
#     print(f'{x1} > {x2}')
# else:
#     print(f'{x2} >= {x1}')
#
#
#
# x3 = x1 * 3


# class A(list):
#     pass
#
#
# obj = A()
# print(type(obj))
#
# obj.append(1)
# print(obj)
#
# class B(int):
#     def __str__(self):
#         return f'{super().__str__()} from B'
#
# obj = B('7')
# print(obj + 5)
# print(obj)



# from abc import ABC, abstractmethod
# class A(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
#
#
# class B(A):
#     def pay(self):
#         print('pay')
#
# x = B()
# x.pay()


class A:
    def pay(self):
        raise NotImplementedError


class B(A):
    def pay(self):
        print('pay')



x = B()
x.pay()

y = A()
y.pay()