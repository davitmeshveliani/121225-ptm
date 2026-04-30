# import datetime
#
# class Student:
#     def __init__(self, first_name, last_name, date_of_birth: str, passport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.passport = passport
#         print(self)
#
#     def age(self):
#         d_birth = datetime.datetime.strptime(self.date_of_birth, "%d/%m/%Y")
#         current_date = datetime.date.today()
#         return current_date.year - d_birth.year - ((current_date.month, current_date.day) < (d_birth.month, d_birth.day))
#
#
# st_1 = Student('Alice', 'Smith', '01/01/1991', 'AA3456789')
# print(st_1.first_name)
# print(hex(id(st_1)))
# print(st_1.age())
#
# st_2 = Student('Anna', 'Smith', '01/01/1990', 'AA3456776')
# print(st_2.first_name)
# print(hex(id(st_2)))
# print(st_2.age())




