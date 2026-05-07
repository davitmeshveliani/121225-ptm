# # SINGLE
# class A:
#
#     def greetings(self):
#         return 'Hello from A'
#
#
# class B(A):
#     pass
#
#
# obj = B()
# print(obj.greetings())
#
#
#
#
# # MULTI LEVEL
# class A1:
#
#     def greetings(self):
#         return 'Hello from A1'
#
#
# class B1(A1):
#
#     def greetings(self):
#         return f'{super().greetings()} & Hello from B1'
#
# class C1(B1):
#     pass
#
#
# obj1 = C1()
# print(obj1.greetings())
#
#
#
#
# class A2:
#     def greetings(self):
#         return 'Hello from A2'
#
#     def f1(self):
#         return 'Hello from A2'
#
#
# class B2:
#     def greetings(self):
#         return 'Hello from B2'
#
#
# class C2(B2, A2):
#     pass
#
#
# obj2 = C2()
# print(obj2.greetings())
# print(obj2.f1())
#
# print(C2.__mro__)


# class A:
#     def __init__(self, a):
#         self.a = a
#
#
# class B(A):
#     def __init__(self, a, b, **kwargs):
#         super().__init__(a, **kwargs)
#         self.b = b
#
#
# class C(A):
#     def __init__(self, a, c, **kwargs):
#         super().__init__(a, **kwargs)
#         self.c = c
#
# class D(B, C):
#     def __init__(self, a, b, c, d):
#         super().__init__(a=a, b=b, c=c)
#         self.d = d
#
#
# print(D.__mro__)
# obj = D(1, 2, 3, 4)
#
# class SaveToFileMixin:
#     def save_to_file(self, filename):
#         f = open(filename, 'w')
#         for k, v in self.__dict__.items():
#             f.write(f'{v}\n')
#         f.close()
#
#
# class AuthMixin:
#     def is_auth(self):
#         if not hasattr(self, 'username') or not hasattr(self, 'password'):
#             return False
#
#         if not self.username or not self.password:
#             return False
#
#         return True
#
#
# class Cat(SaveToFileMixin, AuthMixin):
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Banana(SaveToFileMixin, AuthMixin):
#
#     def __init__(self, name):
#         self.name = name
#
#
# cat1 = Cat(4, 5)
# banana1 = Banana('banana')
#
# cat1.username = 'Tom'
# cat1.password = '<PASSWORD>'
#
# print(cat1.is_auth())
# print(banana1.is_auth())








