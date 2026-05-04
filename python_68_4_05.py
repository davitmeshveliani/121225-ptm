class Student:
    count = 0
    # def __new__(cls, *args, **kwargs): # 1
    #     pass

    def __init__(self, first_name, last_name): # 2
        self.first_name = first_name
        self.last_name = last_name

        Student.count += 1

    @classmethod
    def number_students(cls):
        return cls.count

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return ','.join(map(str, self.__dict__.items()))



st1 = Student('John', 'Doe')
st2 = Student('Alice', 'Smith')

print(st1)
print(repr(st1))

# x = str(st1)
#
# st1.__str__()

# print(Student.number_students())
# print(st1.number_students())

# print(Student.__dict__)

# st1.count += 1 # self.__dict__.get('count', 0) + value
# Student.count += 1
#
# print(Student.count)

# st1.count += 1
# print(st1.__dict__)
# st1.__dict__['city'] = 'Berlin'
#
# print(st1.city)
#
# print(st1.city) # st1.__dict__['city']
# # print(st2.city)
# st1.age = '01/01/2000'
# print(st1.__dict__)


# print(Student.count)
# print(st1.count)
# print(Student.count)


# print(st1.__dict__)
# print(st2.__dict__)
#
# print(Student.__dict__)
# print(st1.first_name)
# print(st2.first_name)
#
#
# print(Student.count)
# print(st1.count)


# def greetings(name: str) -> str:
#     """
#     Return a greetings function
#     """
#     return f'Hello {name}'
#
#
# print(greetings.__dict__)
#
# print(dir(greetings))
# print(dir(st1))
