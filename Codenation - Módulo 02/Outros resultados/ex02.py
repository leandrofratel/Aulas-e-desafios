from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary

    @abstractmethod
    def calc_bonus(self):
        pass
    
    @abstractmethod
    def get_hours(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, department):
        self.__departament.name = department 


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, name):
        self.__departament.name = name

    def calc_bonus(self):
        return self.__sales * 0.15