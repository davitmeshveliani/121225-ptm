# def number_2(n):
#     for i in range(1, n + 1):
#         yield i ** 2
#
#
# def number_3(n):
#     for i in range(1, n + 1):
#         yield i ** 3
#
#
# def numbers(x1, x2):
#     yield from number_2(x1)
#     yield from number_3(x2)


# for number in numbers(5, 10):
#     print(number)


# def flatten(seq):
#     for item in seq:
#         if isinstance(item, list):
#             yield from flatten(item)
#         else:
#             yield item
#
#
# numbers = [1, [2, 3, [4, 5], 6], 7, 8]
# for number in flatten(numbers):
#     print(number)
#
# print(list(flatten(numbers)))


# def process_files(*generators):
#     for gen in generators:
#         yield from gen
#
#
# f1 = open('test_1.txt')
# f2 = open('test_2.txt')
#
# x1 = (int(item) for item in f1 if item.strip().isdigit())
# x2 = (int(item) for item in f2 if item.strip().isdigit())
#
# # for line in process_files(x1, x2):
# #     print(line)
#
#
#
# print(sum(process_files(x1, x2)))


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f'{self.name}: ${self.price}'


# class Cart:
#     def __init__(self):
#         self.products = []
#         self.quantities = []
#
#     def add_product(self, product, quantity=1):
#         if not isinstance(product, Product):
#             raise TypeError('Product must be of type Product.')
#
#         if not isinstance(quantity, int | float):
#             raise TypeError('Quantity must be of type int or float.')
#
#         if quantity <= 0:
#             raise ValueError('Quantity must be greater than 0.')
#
#         self.products.append(product)
#         self.quantities.append(quantity)
#
#     def total(self):
#         return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))
#
# from collections import defaultdict
#
# class Cart:
#     def __init__(self):
#         self.items = defaultdict(float)
#
#     def add_product(self, product, quantity=1):
#         if not isinstance(product, Product):
#             raise TypeError('Product must be of type Product.')
#
#         if not isinstance(quantity, int | float):
#             raise TypeError('Quantity must be of type int or float.')
#
#         if quantity <= 0:
#             raise ValueError('Quantity must be greater than 0.')
#
#         self.items[product] += quantity
#
#     def total(self, user):
#         return sum(product.price * quantity for product, quantity in self.items.items()) * (1 - user.discount)
#
#
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.discount = 0.0
#
#
#
#
#
#
# p1 = Product("Banana", 100)
# p2 = Product("Kiwi", 200)
# p3 = Product("Apple", 300)
# p4 = Product("Tomatos", 400)
# p5 = Product("Grape", 600)
#
# # print(p1)) # str  = p1.__str__()
#
# user_1 = User("Oleh", "Tymchuk")
# user_1.discount = 0.1
# user_2 = User("Anton", "Trofimov")
# user_2.discount = 0.2
#
# order_Oleh = Cart()
# order_Oleh.add_product(p1, 2)
# order_Oleh.add_product(p2, 2)
# order_Oleh.add_product(p3, 1.5)
#
#
# order_Anton = Cart()
# order_Anton.add_product(p1, 1)
# order_Anton.add_product(p4, 1)
# order_Anton.add_product(p5, 0.5)

# print(*order_Oleh.products, sep='; ')
# print(order_Oleh.quantities)
# print(order_Oleh.total())
#
# print(*order_Anton.products, sep='; ')
# print(order_Anton.quantities)
# print(order_Anton.total())

# print(*order_Oleh.items.items(), sep='; ')
# print(order_Oleh.total(user_1))
#
# print(*order_Anton.items.items(), sep='; ')
# print(order_Anton.total(user_2))


# print(p1.name, p1.price)

# print(p1)
# print(p1.name)
# print(hex(hash(p1)))


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.last_name}, {self.first_name[0]}.'


class Group:
    def __init__(self, name, limit=3):
        self.name = name
        self.students = []
        self.limit = limit

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError('Student must be of type Student.')

        if student in self.students:
            raise ValueError(f'Student {student} already added.')

        if len(self.students) >= self.limit:
            raise ValueError(f'Group limit exceeded.')

        self.students.append(student)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.students))


if __name__ == '__main__':
    s1 = Student('John', 'Smith1')
    s2 = Student('Alice', 'Smith2')
    s3 = Student('Bob', 'Smith3')
    s4 = Student('Anna', 'Smith4')

    g1 = Group('121225')

    g1.add_student(s1)
    g1.add_student(s2)
    g1.add_student(s3)

    print(g1)




