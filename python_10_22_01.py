# print(2 ** 3)
# print(pow(2, 3))
#
# print(pow(2, 3, 7)) # 2 ** 3 % 7
#
# res = min(1, 2, 3, 4, -1)
# print(res)
#
# x = [1, 2, 3, -1, 4]
# res = min(x)
# print(res)
#
# res = sum([1, 2, 3, 4])
# print(res)
import math

# print(round(4.56))
# print(round(4.567, 2))
# print(round(4.5))
# print(round(5.5))
# print(round(4.52))
# print(round(5.52))

#
# import math
# print(math.factorial(5))
#
#
# import math as m
# print(m.factorial(5))
#
#
# from math import factorial
#
# print(factorial(5))
#
# from math import * # BAD style

# import sys
#
# print(*sys.stdlib_module_names, sep='\n')


# import math
# print(100 ** 300)
# print(math.pow(100, 300))

# import sys
#
# print(sys.float_info)

#
# print(0.1 + 0.1 + 0.1 == 0.3)
#
# x = 2.675 # 2.6749999999999998
# print(round(x, 2) == 2.68)

x = 2.675
y = 2.68
res = math.isclose(x, y, rel_tol=0.01)
print(res)









