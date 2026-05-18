# class EmployeeSalary:
#
#     def __init__(self, name, salary, tax_rate=0.2):
#         self.name = name
#         self.salary = salary
#         self.tax_rate = tax_rate
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         if not isinstance(value, int | float):
#             raise TypeError('Salary must be an integer or float')
#
#         self.__salary = value
#
#     def netto(self):
#         return self.salary * (1 - self.tax_rate)



# x1 = EmployeeSalary('<NAME>', 10000)
# x2 = EmployeeSalary('<NAME>', 12000)
# x3 = EmployeeSalary('<NAME>', 12000)
#
# employees = [x1, x2, x3]
# res = x1.netto()
#
# print(res)
#

# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError('radius cannot be negative')
#         self.__radius = value
#
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def length(self):
#         return 2 * math.pi * self.radius
#
#
# x = Circle(-5)
# x.radius = 'Hello'
# print(x.length())


import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_DATABASE', 'test'),
}

conn = pymysql.connect(**config)
if conn.open:
    print('Connection opened')


    cursor = conn.cursor()

    # result = cursor.execute('select * from departments')
    #
    # print(type(result))
    # for row in cursor:
    #     print(row)
    #
    # user_input = input('Enter your id: ')
    # sql = f"SELECT * FROM employees WHERE employee_id = {user_input}"
    #
    # cursor.execute(sql)
    #
    # for row in cursor:
    #     print(row)
    #
    # cursor.execute(sql)

    cursor.execute('SHOW TABLES')
    for table in cursor.fetchall():
        print(table)
    print('-' * 50)
    cursor.execute('DESCRIBE departments')
    for table in cursor.fetchall():
        print(table)

    cursor.close()
conn.close()



