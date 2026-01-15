# Тестирование объекта на truth

# x = 0
# print(bool(x))
# x = 100
# print(bool(x))
# x = -100
# print(bool(x))
#
# # Numbers as False - 0, 0.0, 0j, False
# # Seq as False - пустая последовательность, т.е. в которой нет ни одного элемента, '', [], (), {}, set()
# # None - False
# print(23e-2)
# print(0.23e2)


# name = input("Enter your name: ")
# Bad style
# if len(name) > 0:
#     print(name.upper())
# else:
#     print("Name cannot be empty")

#
# if name:
#     print(name.upper())
# else:
#     print("Name cannot be empty")
#
#
# if "":
#     print("NO")
# else:
#     print("YES")
#

# a = int(input('Enter a number: '))
#
# if not a % 2:
#     print(a ** 3)

#
# name = input("Enter your name: ")
# if not name:
#     print("Please enter your name")

#
# salary = int(input('Enter your salary: '))
# res_1 = salary >= 2000 and salary <= 5000 # bad style
#
# res_1 = 2000 <= salary <= 5000
#
# print('In 2000-5000:', res_1 )
#
# res_2 = salary < 2000 or salary > 5000
# print('Not In 2000-5000:', res_2 )
# print('Not In 2000-5000:', not res_1)


a = 0
b = 6

res = a or b
print(res, bool(res))







