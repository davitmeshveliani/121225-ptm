class Student:
    """
    Define a class Student.
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}.'

    def __repr__(self):
        return f'Student(first_name={self.first_name}, last_name={self.last_name})'

# class GroupIterator:
#     def __init__(self, students):
#         self.students = students
#         self.index = 0
#
#     def __next__(self):
#         if self.index >= len(self.students):
#             raise StopIteration
#
#         self.index += 1
#         return self.students[self.index - 1]


# class Group:
#     def __init__(self, name):
#         self.name = name
#         self.__students = []
#         self.index = 0
#
#
#     def add_student(self, student):
#         self.__students.append(student)
#
#     # def __iter__(self):
#     #     return GroupIterator(self.__students)
#
#     # def __iter__(self):
#     #     return iter(self.__students)
#
#     # def __iter__(self):
#     #     self.index = 0
#     #     return self
#     #
#     # def __next__(self):
#     #     if self.index >= len(self.__students):
#     #         raise StopIteration
#     #
#     #     self.index += 1
#     #     return self.__students[self.index - 1]
#
#     def __iter__(self):
#         for student in self.__students:
#             yield student
#
#     def __len__(self):
#         return len(self.__students)
#
#     def __getitem__(self, index):
#
#         if isinstance(index, slice):
#             tmp_students = self.__students[index]
#
#             new_group = Group(self.name)
#             for student in tmp_students:
#                 new_group.add_student(student)
#             return new_group
#
#         return self.__students[index]
#
#     def __setitem__(self, index, value):
#         if not isinstance(index, int):
#             raise TypeError('index must be an integer')
#         if not isinstance(value, Student):
#             raise TypeError('value must be an instance of Student')
#
#         self.__students[index] = value
#
#
#     def __contains__(self, student):
#         return student in self.__students
#
#     def __str__(self):
#         return '\n'.join(str(student) for student in self)
#
#
# st1 = Student('John', 'Smith')
# st2 = Student('Alice', 'Ivanova')
# st3 = Student('Bob', 'Smith')
# st4 = Student('Jack', 'Smith')
#
# gr1 = Group('Python')
# gr1.add_student(st1)
# gr1.add_student(st2)
# gr1.add_student(st3)
# gr1.add_student(st4)
#
# for student in gr1:
#     print(student)
#
# for student in gr1:
#     print(student)
#
# print(len(gr1))
#
# print(gr1[::-1])
#
# print(st1 in gr1)
#
# gr1[1] = Student('John1', 'Smith1')



# from functools import total_ordering
#
# @total_ordering
# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def volume(self):
#         return self.x * self.y * self.z
#
#     def __gt__(self, other):
#         return self.volume() > other.volume()
#
#     def __eq__(self, other):
#         return self.volume() == other.volume()
#
#     def __str__(self):
#         return f'{self.x} x {self.y} x {self.z}'
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#            return Box(self.x * other, self.y * other, self.z * other)
#
#         return NotImplemented
#
#         # self.x *= other
#         # self.y *= other
#         # self.z *= other
#         # return self
#
#     def __imul__(self, other):
#         self.x *= other
#         self.y *= other
#         self.z *= other
#         return self
#
#     def __rmul__(self, other):
#         return Box(self.x * other, self.y * other, self.z * other)
#
#     def __bool__(self):
#         return self.volume() > 0

#
# box_1 = Box(10, 2, 3)
# box_2 = box_1 * 2
#
# print(box_1)
# print(box_2)
#
#
# box_1 *= 3
# print(box_1)
#
#
# box_4 = 3 * box_1 # (3).__mul__(box_1)
# print(box_4)


# x = 'Hello' * 3
# print(x)


# Iterator Protocol: __iter__, __next__
# Sequence Protocol: __getitem__, __len__



# box1 = Box(10,1,0)
# if box1:
#     print('Box exists')
# else:
#     print('Box does not exist')



class USDEURConvertor:
    def __init__(self, index):
        self.index = index

    def __call__(self, value, *args, **kwargs):
        return value * self.index


# usdeur = USDEURConvertor(0.85)
#
# print(usdeur.convert(1000))
# print(usdeur.convert(100))


usdeur = USDEURConvertor(0.85)

print(usdeur(1000))
print(usdeur(100))
