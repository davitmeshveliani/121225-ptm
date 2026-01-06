# 1. Переменные и id объекта
x = 5
print(id(x))     # id — уникальный идентификатор объекта в памяти

y = 1
print(id(y))

x = x + y        # создаётся НОВЫЙ объект
print(id(x))
print(x)


# 2. Типы данных


print(type(5))   # int — целое число

x = 100
x = -200
x = 1_000_000    # подчёркивание — просто для удобства чтения
x = 111111111111111111111111111111111111111111111111111111
print(x)


# 3. Числа с плавающей точкой (float)


x = 5.
print(x)

x = .001
print(x)


# 4. Строки


# Строка с управляющим символом \n (перенос строки)
x = 'Hello\nPython'
print(x)

# Многострочная строка
x = """
Hello
Python
"""
print(x)


# 5. Логический тип данных


y = False
x = True          # тип переменной можно менять
print(x)


# 6. None


a = None          # означает "ничего", "пусто"
print(a)


# 7. input и print


name = input('name>> ')
print(name)

# print ничего не возвращает
x = print(name)
print(x)          # None


# 8. print — это тоже объект

x = print
x('Hello, Oleh')


# 9. Работа с type


x = 5
res = type(x)

print(res.__name__)   # имя типа
print(type(res))      # type — это тоже тип


# 10. Арифметика (базово)


x = 5
y = 6
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)


# 11. Операции со строками


x = 'Hello'
y = 'world'

print(x + ' ' + y)    # конкатенация строк
print(x, y)           # print сам добавляет пробел

print('+' + '10')     # строки не становятся числами
print(10 * '-')       # повторение строки


# 12. Экранирование символов


x = 'users\'s name'
print(x)

x = 'users\nname'
print(x)

x = 'users\n\tname'
print(x)


# 13. print с параметром end


print(1, 2, 3, 4, end='****')
print(5, end='!!!')
print(6)
