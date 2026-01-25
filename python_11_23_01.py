# try:
#     a = int(input("Enter a number: "))
# except ValueError:
#     print("Enter a number")
# except TypeError:
#     print("Enter a number")


# number = int(input("Enter a number:"))
#
# if number % 2:
#     res = number ** 2
# else:
#     res = number ** 3
#
#
# res = number ** 2 if number % 2 else number ** 3
# print(res)

# x = [2, 3, 4, -5, -6]
# y = [True, True, True, False, False]
#
# print(sum(y))
# print(12 + True)
#
# print(bool(0), bool(0.0), bool(None))
# print(bool([]), bool(''), bool({}))

# number = int(input('Enter number:'))
# if number % 2:
#     print("значение:", number ** 2)
# else:
#     print("значение:", number ** 3)
#
#
# print("значение:", number ** 2) if number % 2 else print("значение:", number ** 3)
#
# year = 2024
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap year')
#         else:
#             print('Not a leap year')
#     else:
#         print('Leap year')
# else:
#     print('Not leap year')
#
#
# if year % 4 == 0 and year % 100 != 0:
#     print('Leap year')
# else:
#     if year % 400 == 0:
#         print('Leap year')
#     else:
#         print('Not a leap year')
#
#
# if year % 4 == 0 and year % 100 != 0:
#     print('Leap year')
# elif year % 400 == 0:
#     print('Leap year')
# else:
#     print('Not a leap year')
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Leap year')
# else:
#     print('Not a leap year')
#
# y = not 5
# print(y)
#
# y = 6 or 0
# print(bool(y))
#
# y = '' and 6
# print(bool(y))
#
# y = 0 or None
# print(y)

#
# x = 0.1
# y = 0.3

# print(x + x + x == y)

# import decimal
#
# x = decimal.Decimal('0.1')
# y = decimal.Decimal('0.3')
#
# res = x + x + x
#
# print(res, type(res))

# from decimal import Decimal
# x = Decimal(0.1)
# y = Decimal(0.3)
#
# print(x + x + x == y)

# from decimal import Decimal, ROUND_HALF_UP
#
# x = Decimal('2.5445')
# print(x)
#
# y = x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
# print(y)
# str(5.6)
# print((0.1+0.1+0.1).__str__())


filename = input("Enter a file name: ")

# txt, csv, json, pdf, unknown
match filename:
    case _ if filename.endswith('.txt'):
        print('Text File in plain text')
    case _ if filename.endswith('.csv'):
        print('Text File with comma')
    case _ if filename.endswith('.json'):
        print('Text File as Java Script')
    case _ if filename.endswith('.pdf'):
        print('Text File as PDF')
    case _:
        print('Unknown Format')

x, y = int(input("Enter x: ")), int(input("Enter y: "))

match (x, y):
    case _ if x > 0 and y > 0:
        print('1')
    case _ if x < 0 and y < 0:
        print('3')
    case _ if x < 0 and y > 0:
        print('2')
    case _ if x > 0 and y < 0:
        print('4')
    case _ if x == 0 and y == 0:
        print('0')
    case _ if x == 0:
        print('Y')
    case _:
        print('X')