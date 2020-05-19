class Department():
    """Inicializa a classe 'Department'."""
    
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee():
    """Inicializa a classe 'Employee'."""

    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary
        self.__workload = 8

    def calc_bonus(self):
        return 0

    def get_hours(self):
        return self.__workload

    def get_salary(self):
        return self.__salary


class Manager(Employee):
    """Inicializa a classe 'Manager'."""
    
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, department):
        self.__departament.name = department

    def calc_bonus(self):
        return self.get_salary() * 0.15


class Seller(Manager):
    """Inicializa a classe 'Seller'."""
    
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, department):
        self.__departament.name = department

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales = self.__sales + sales

    def calc_bonus(self):
        return self.get_sales()*0.15
