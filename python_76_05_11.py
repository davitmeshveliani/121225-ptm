from abc import ABC, abstractmethod, abstractproperty


# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self):
#         pass


# class PaymentProcessor:
#     """
#
#     """
#     def pay(self):
#         raise NotImplementedError
#
#
# class CreditPaymentProcessor(PaymentProcessor):
#
#     def pay(self):
#         return 'credit card payment'
#
# class DebitPaymentProcessor(PaymentProcessor):
#
#     def pay(self):
#         return 'debit card'
#
#
# class CryptoProcessor(PaymentProcessor):
#     def pay(self):
#         return 'usdt crypto'
#
#
# def payment_processor(processor):
#     return processor.pay()
#
#
# payment_methods = ['credit card', 'debit card', 'usdt']
# answer = input(f'How would you like to pay?\n' + '; '.join(payment_methods))
# if answer == 'credit card':
#     processor = CreditPaymentProcessor()
# elif answer == 'debit card':
#     processor = DebitPaymentProcessor()
# elif answer == 'usdt':
#     processor = CryptoProcessor()
#
# print(payment_processor(processor))

# class GroupLimitError(ValueError):
#     pass
#
# class StudentExistsError(ValueError):
#     pass
#
#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return f'Student=(name={self.name})'
#
#
# class Group:
#     LIMIT = 3
#     def __init__(self, name):
#         self.name = name
#         self.__students = []
#
#     def add_student(self, student: Student) -> None:
#         if not isinstance(student, Student):
#             raise TypeError('Student must be of type Student')
#
#         if student in self.__students:
#             raise StudentExistsError('Student already added')
#
#         if len(self.__students) >= self.LIMIT:
#             raise GroupLimitError('Student already added')
#
#         self.__students.append(student)
#
#
# st1 = Student('John')
# st2 = Student('Mary')
# st3 = Student('Jack')
# st4 = Student('Jim')
# st5 = Student('Alice')
# st6 = Student('Bob')
#
# students = [st1, st2, st3, st3, st4, st4, st5, st6]
# groups = []
#
#
# for student in students:
#     try:
#         current_group = groups[-1] if groups else Group(f'Python {len(groups) + 1}')
#         if not groups:
#             groups.append(current_group)
#         current_group.add_student(student)
#     except ValueError:
#         print('Error')
#
#     # except StudentExistsError as e:
#     #     continue
#     # except GroupLimitError:
#     #     tmp = Group(f'Python {len(groups) + 1}')
#     #     groups.append(tmp)
#     #     tmp.add_student(student)
#


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __eq__(self, other):
        return self.volume() == other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __ne__(self, other):
        return self.volume() != other.volume()

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


box_1 = Box(10, 2, 3)
print(box_1)

box_2 = Box(2, 3, 4)
print(box_2)

# print(box_1.volume() > box_2.volume())

print(box_1 > box_2) # box_1.__gt__(box_2)


import random

boxes = [Box(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for _ in range(10)]
print(*boxes, sep='\n')
print('-' * 50)
print(min(boxes))
print(max(boxes))
print('-' * 50)
boxes.sort()
print(*boxes, sep='\n')



# x = 4 + 5
# x = (4).__add__(5)
# print(x)