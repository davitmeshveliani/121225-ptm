# # class A:
# #     pass
# #
# #
# # x = A()
# # print(x.__str__())
# # print(A.__mro__)
#
#
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def work(self):
#         return f'Employee {self.name} is working...'
#
#
# class Developer(Employee):
#     def coding(self):
#         return f'{self.name} is coding...'
#
#     def work(self):
#         res = super().work()
#         return f'*{res}*'
#
# print(Developer.__mro__)
#
#
# class Manager(Employee):
#     def work(self):
#         return f'{self.name} doesnot work...'
#
#     def __str__(self):
#         return 'Manager'
#
#
# x1 = Developer('John')
# x2 = Manager('Mary')
#
# print(x1.work())
# print(x1.coding())
# print(x2.work())
# print(x1)
# print(x2)
#
#
# class A:
#     def greetings(self):
#         return f'Hello from A'
#
#
# class B(A):
#     def greetings(self):
#         return f'Hello from B'
#
#
# class C(B):
#     def greetings(self):
#         return f'Hello from C'
#
#
# print(C.__mro__)
#
# x = C()
# print(x.name)

#
#
#
#
# class A:
#     ...
#
# class B(A):
#     ...
#
# class C(A):
#     ...
#
# class D(B, C):
#     ...
#
#
# print(D.__mro__)



# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#
# class Programmer(Employee):
#     def __init__(self, name, language):
#         super().__init__(name)
#         self.language = language
#
#
# class Manager(Employee):
#     def __init__(self, name, department):
#         super().__init__(name)
#         self.department = department
#
#
# x1 = Programmer('Python', 'Java')
# print(x1.name)


#
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"Init Person: {self.name}")
#
# class Employee(Person):
#
#     def __init__(self, name):
#         super().__init__(name)
#         print(f"Init Employee: {self.name}")
#
#     def work(self):
#         print(f"{self.name} is working...")
#
# class Manager(Employee):
#     def __init__(self, name, department):
#         super().__init__(name)
#         self.department = department
#         print(f"Init Manager: {self.name} manages {self.department}")
#
# m = Manager("Alice", "Development")



class School:
    data = None
    def __new__(cls, *args, **kwargs):
        if cls.data is None:
            self = super().__new__(cls)
            cls.data = self
            return self

        return cls.data

    def __init__(self, name):
        self.name = name

x1 = School('ICH')
print(id(x1))
print(x1.name)
x2 = School('ICH 2')
print(id(x2))
print(x2.name)





