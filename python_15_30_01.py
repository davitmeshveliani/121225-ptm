# text = '43453453452026'
# y = len(text)
# print(y)
#
#
# y = text.upper()
# print(y)
#
# y = text.isdigit()
# print(y)
#
# print(chr(2000))
# print(ord('H'))
#
# text = 'Hello'
# i = 0
# while i < len(text):
#     print(ord(text[i]))
#     i += 1

#
# text = 'Hello'
# i = 0
# while i < len(text) :
#     i += 1
#     print(ord(text[i]))


# t = int(input('T>>'))
# if t < -20:
#     print('Stay at home')
# print('Have a nice day!')



# if t < 0:
#     print('It is cold')
# else:
#     print('It is normal')
# print('Have a nice day!')


# if t < -20:
#     print('Stay at home')
# elif t < 0:
#     print('It is cold')
# else:
#     print('It is normal')
#
# print('Have a nice day!')

#
# if t < -20:
#     print('Stay at home')
# elif t < 0:
#     print('It is cold')
# else:
#     shopping = input('Maybe shopping?').lower().strip()
#     if shopping == 'yes': # YES, Yes,   yes
#         print('You need $')
#     else:
#         print('Ok!')
#     print('It is normal')
#
# print('Have a nice day!')

# x = 'Hello world!'
#
# print(x[1:])
#
#
# y = 'Y' + x[1:]
# print(y)
#
# y = x[:-3]
# print(y)
#
# print(x[2:-2])
#
# print(x[::-1])
#
# x = '12345678'
# print('Palindrome' if x == x[::-1] else 'Not Palindrome')

# y = x[3:9]
# print(y)
# print(x)
#
#
# y = x[3:9:2]
# print(y)


# x = 'Hello'
# print('ll' in x)
# print('LL' in x)
#
# print('ll' not in x)
# print('LL' not in x)
#
# print('eo' not in x)
#
# print('o' in x)
#
# print(x.count('l'))


import random


secret = random.randint(1, 100)
ATTEMPTS = 3
iswin = True
i = 0

while i < ATTEMPTS:
    user_number = int(input('Enter a number: '))
    i += 1
    if user_number < secret:
        print('Secret number is greater')
    elif user_number > secret:
        print('Secret number is less')
    else:
        print('Congratulations!')
        print('You use ', i, 'attempts')
        break
else:
    iswin = False
    print('You lose')


if iswin:
    ...







