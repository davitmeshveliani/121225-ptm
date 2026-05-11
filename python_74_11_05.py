# class A:
#
#     def __init__(self, a):
#         self.a = a
#
#
# class B(A):
#
#     def __init__(self, a, b, *args, **kwargs):
#         super().__init__(a=a)
#         self.b = b
#
#
# class C(A):
#     def __init__(self, a, first_name, last_name):
#         super().__init__(a)
#         self.first_name = first_name
#         self.last_name = last_name
#
#
# class D(B, C):
#     def __init__(self, a, b, c):
#         super().__init__(a, b)
#
#
# x = D(1, 2, 3)

# class Address:
#     def __init__(self, street, city, country, house_number, apartment=None):
#         self.street = street
#         self.city = city
#         self.country = country
#         self.house_number = house_number
#         self.apartment = apartment


# class Student:
#
#     def __init__(self, first_name, last_name, street, city, country, house_number, apartment=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = Address(street, city, country, house_number, apartment)
#
#
# st1 = Student('John', 'Smith', street='Av1', city='San Francisco', country='USA', house_number=1)
#
# print(st1.address.city)

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = []
#
#
#
# st1 = Student('John', 'Smith')
#
# addr1 = Address(street='Av1', city='San Francisco', country='USA', house_number=1)
# addr2 = Address(street='Av1', city='San Francisco', country='USA', house_number=2)
#
# st1.address.append(addr1)
# st1.address.append(addr2)
#
# print(st1.address)




class Student:

    def __init__(self, first_name, last_name, address, passport):
        self.first_name = first_name    # public
        self.last_name = last_name      # public
        self._address = address         # protected
        self.__passport = passport      # private


class PartTimeStudent(Student):
    def __init__(self, first_name, last_name, address, passport, date_of_birth):
        super().__init__(first_name, last_name, address, passport)
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self._address}'


x = PartTimeStudent('John', 'Doe', 'john@gmail.com', '123456', '01/01/2000')
# print(x.first_name)
# print(x.last_name)
# print(x._address)
# print(x.__passport)
# x._Student__passport = 1234567890000000
# print(x._Student__passport)

# print(x.first_name)
# print(x.last_name)
#
# print(x.date_of_birth)

# print(x._address)

# x._Student__kuku = 'trulala'
# print(x.__dict__)






