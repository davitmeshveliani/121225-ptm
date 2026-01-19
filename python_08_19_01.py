# # One branch
# t = int(input('T>>'))
#
# if t < 0:
#     print('Hello')
#     print('It is cold!')
#
#
# print('Have a nice day!')

# name = input("Enter your name: ")
#
# if len(name) > 0: # BAD STYLE
#     print(name.upper())
#
# if name: # COOL STYLE
#     print(name.upper())


# # Two branches
# t = int(input('T>'))
#
# if t < 0:
#     print('It is cold')
# else:
#     print('It is normal')
#
# print('Have a  nice day!')

#
# number = int(input("Enter a number: "))
#
# # BAD STYLE
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
#
# # GOOD STYLE
# if number % 2:
#     print("odd")
# else:
#     print("even")


# t = int(input('T>'))
#
# if t > 10:
#     money = float(input('Money>'))
#     if money > 100:
#         print('Go to shopping')
#     else:
#         print('Not enough money')
# else:
#     print('Bad weather')


#
# salary = int(input('Enter your salary: '))
#
# # BAD
# if salary <= 1000:
#     print('Taxes = 10%')
# else:
#     if salary < 2000:
#         print('Taxes = 20%')
#     else:
#         if salary <= 4000:
#             print('Taxes = 40%')
#         else:
#             print('Taxes = 50%')
#
#
# if salary <= 1000:
#     print('Taxes = 10%')
# elif salary < 2000:
#     print('Taxes = 20%')
# elif salary <= 4000:
#     print('Taxes = 40%')
# else:
#     print('Taxes = 50%')



# a = 10
# if a == 10:
#     print(10)
#     a = 0
# elif a == 0:
#     print(0)
#     a = 100
# elif a == 200:
#     print(200)
# else:
#     print(a)
#
# print(a)

#
# a = 10
# if a == 10:
#     print(10)
#     a = 0
# if a == 0:
#     print(0)
#     a = 100
# if a == 200:
#     print(200)
# else:
#     print(a)
#
# print(a)
#


# salary = 1000
#
# if salary <= 1000:
#     print('Taxes = 10%')
# elif salary < 2000:
#     print('Taxes = 20%')
# elif salary <= 4000:
#     print('Taxes = 40%')
# else:
#     print('Taxes = 50%')



# if salary <= 1000:
#     print('Taxes = 10%')
#
# if salary < 2000:
#     print('Taxes = 20%')
#
# if salary <= 4000:
#     print('Taxes = 40%')
# else:
#     print('Taxes = 50%')


# t = int(input('T>>'))
# money = float(input('Money>>'))
#
# # BAD
# if t > 10:
#     if money > 100:
#         print('Shopping')
#
# # GOOD
# if t > 10 and money > 100:
#     print('Shopping')


# points = float(input("Enter a number: "))
#
# if points < 0 or points > 100:
#     print("Invalid number")
# elif points < 60:
#     print('F')
# elif points < 70:
#     print('E')
# elif points < 75:
#     print('D')
# elif points < 80:
#     print('C')
# elif points < 90:
#     print('B')
# else:
#     print('A')



salary = int(input('Enter your salary: '))
# 4 lines, 2 branches, 1 var, simple expr
if salary < 4000:
    taxes = 0.25
else:
    taxes = 0.5

print('Tax rate:', taxes)
netto = salary * (1 - taxes)
print('Netto:', netto)



# taxes = 0.25 if salary < 4000 else 0.5
# print('Tax rate:', taxes)

netto = (1 - 0.25 if salary < 4000 else 0.5) * salary
print('Netto:', netto)









