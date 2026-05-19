import os
from dataclasses import dataclass
from collections import namedtuple

import pymysql
from dotenv import load_dotenv


load_dotenv('.env')


config = {'host': os.getenv('DB_HOST'),
          'user': os.getenv('DB_USER'),
          'password': os.getenv('DB_PASSWORD'),
          'database': os.getenv('DB_DATABASE'),
          }

CurrentEmployee = namedtuple('CurrentEmployee', ['firstName', 'lastName', 'job', 'salary'])


# @dataclass(frozen=True)
# class CurrentEmployee:
#         first_name: str
#         last_name: str
#         job_title: str
#         salary: int | float



class Employee:
    DEPARTMENTS_QUERY = """
         SELECT department_name
         FROM departments
    """


    EMPLOYEES_QUERY = """
        SELECT first_name, last_name, job_title, salary
        FROM employees
        JOIN departments ON employees.department_id = departments.department_id
        JOIN jobs ON employees.job_id = jobs.job_id
        WHERE departments.department_name = %s
        {salary_filter}
        ORDER BY salary DESC
    """

    def __init__(self, cur):
        self.cur = cur

    def get_departments(self):
        self.cur.execute(self.DEPARTMENTS_QUERY)
        return [row[0] for row in self.cur]

    def get_employees(self, department, salary_filter=''):
        self.cur.execute(self.EMPLOYEES_QUERY.format(salary_filter=salary_filter), (department,))
        return [CurrentEmployee(*row) for row in self.cur]


# UI

def print_departments(departments):
    for index, department in enumerate(departments, start=1):
        print(index, department)


def print_employees(employees):
    for index, employee in enumerate(employees, start=1):
        print(index, employee)


def prompt_departments(departments):
    while True:
        try:
            number = int(input('Enter department number: '))
            if 1 <= number <= len(departments):
                return departments[number - 1]
            raise IndexError
        except ValueError:
            print('Invalid department number')
        except IndexError:
            print(f'Department number must be between 1 and {len(departments)}')




def main():
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cur:
            employee = Employee(cur)
            departments = employee.get_departments()
            print_departments(departments)
            department = prompt_departments(departments)
            print(f'You chose department {department}')
            employees = employee.get_employees(department)
            print_employees(employees)

            for employee in employees:
                print(employee[0])
                print(type(employee))







if __name__ == '__main__':
    main()