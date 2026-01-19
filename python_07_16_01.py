# x = 7
# y = 7
#
# print(id(x))
# print(id(y))
#
# y += 1
#
# print(x)
# print(y)
# print(id(x))
# print(id(y))

# def func(a=[]):
#     a.append(1)
#     return a
#
#
# print(func())
# print(func())
# print(func())
#
#
#
# def func(a='Hello'):
#     a += '!'
#     return a
#
#
# print(func())
# print(func())
# print(func())

#
# a, b = 0, 0
# print(id(a), id(b))
# a = b = 0
# print(id(a), id(b))
#
#
# a, b = [], []
# print(id(a), id(b))
# a.append(1)
# b.append(2)
# print(a)
# print(b)
# a = b = []
# print(id(a), id(b))
# a.append(1)
# b.append(2)
# print(a)
# print(b)

#
# # Пользователь вводит средний балл студента.
# # Определите, может ли студент получить скидку на обучение (скидка дается, если средний балл выше 4.5).
# ALLOW_P = 4.5
# points = float(input("Enter points:"))
# res = points > ALLOW_P
# print(res)

# Пользователь вводит два числа. Проверьте, является ли одно из чисел четным, а другое — нечетным.
# a, b = int(input('a>>')),\
#        int(input('b>>'))

# iseven = a % 2 == 0
# isodd = a % 2 != 0


# is_even = not a % 2
# is_odd = bool(b % 2)
#
# print(is_even, is_odd)

# # Пользователь вводит три числа.
# # Проверить, являются ли все три числа положительными или хотя бы одно из них больше 100
# a, b, c = int(input('a>>')), int(input('b>>')), int(input('c>>'))
#
# res = (a > 0 and b > 0 and c > 0) or (a > 100 or b > 100 or c > 100)


# a, b = int(input('a>>')), int(input('b>>'))

# res = (a < 0 and b < 0) or (a > 0 and b > 0)
# res = a * b > 0


# first = input('first value (True/False)>')
# second = input('second value (True/False)>')
#
# first = bool(first == 'True')
# second = bool(second == 'True')

# first = bool(int(input('first value (1 - True/0 - False)>')))  # '1' -> 1 -> True
# second = bool(int(input('second value (1 - True/0 - False)>'))) # '0' -> 0 -> False
#
# print('value 1', 'value 2', 'and', 'or', 'not', sep='\t')
# print(first, second, first and second, first or second, not first, sep='\t')


tariff = float(input("Enter tariff: "))
value_mb = int(input("Enter value: "))


res = 30 + max(value_mb - 500, 0) * 0.2
print(res)


extra_mb = (value_mb - 500) * (value_mb > 500)
res = 30 + extra_mb * 0.2
print(res)



