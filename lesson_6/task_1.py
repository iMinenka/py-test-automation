"""Для задания Company model, замените check_yourself на несколько независимых юнит-тестов, используя при этом Pytest.

Примечания:
•	обязательно использование хотя бы одной фикстуры
•	обязательно использование хотя бы одного пайтест хука
•	обязательно использование хотя бы одной пайтест метки
•	используйте pytest-html плагин для создания HTML репорта
•	используйте pytest-xdist плагин для параллельного запуска тестов
•	параметры для плагинов должны быть заданы в pytest.ini
"""

import abc


class Company(object):
    """ Represents a company """

    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def add_employee(self, employee):
        """Company employs an Engineer or Manager"""
        # make sure employee is an instance of Engineer or Manager
        # make sure he is not employed already
        if isinstance(employee, (Engineer, Manager)):
            if employee not in self.employees:
                self.employees.append(employee)
            else:
                raise ValueError(f"{employee.name} is already employed in {self}")
        else:
            raise ValueError(f"{employee} is not Engineer/Manager")

    def dismiss_employee(self, employee):
        """
        Dismisses an employee. Employee must be a company member.
        Company should notify employee that he/she was dismissed
        """
        self.employees.remove(employee)
        employee.notify_dismissed()

    def notify_im_leaving(self, employee):
        """ En employee should call this method when leaving a company """
        if employee in self.employees:
            self.dismiss_employee(employee)
        else:
            print(f"{self} has no employee {employee.name}")

    def do_tasks(self, employee):
        """
        Engineer should call this method when he is working.
        Company should withdraw 10 money from a personal account and return
        them to engineer. That will be a payment
        :rtype: int
        """
        # make sure engineer is employed to this company
        # check employee is Engineer
        work_pay = 10
        if employee in self.employees:
            if isinstance(employee, Engineer):
                self.__money -= work_pay
                return work_pay
            else:
                print(f"{employee.name} is not Engineer")
        else:
            print(f"{employee.name} is not employed in {self}")

    def write_reports(self, employee):
        """
        Manager should call this method when he is working.
        Company should withdraw 12 money from a personal account and return
        them to manager. That will be a payment
        :rtype: int
        """
        # make sure manager is employed to this company
        # check employee is Manager
        work_pay = 12
        if employee in self.employees:
            if isinstance(employee, Manager):
                self.__money -= work_pay
                return work_pay
            else:
                print(f"{employee.name} is not Manager")
        else:
            print(f"{employee.name} is not employed in {self}")

    def make_a_party(self):
        """ Party time! All employees get 5 money """
        # make sure a company is not a bankrupt before and after the party
        # call employee.bonus_to_salary()
        if not self.is_bankrupt:
            party_budget = len(self.employees) * 5
            if self.__money > party_budget:
                self.__money -= party_budget
                for employee in self.employees:
                    Employee.bonus_to_salary(employee, self)
            else:
                print(f"{self} budget not enough for party, sorry...")
        else:
            print(f"{self} is bankrupt, no party, sorry...")

    def show_money(self):
        """ Displays amount of money that company has """
        return print(self.__money)

    def go_bankrupt(self):
        """
        Declare bankruptcy. Company money are drop to 0.
        All employees become unemployed.
        """
        self.__money = 0
        for employee in self.employees:
            self.dismiss_employee(employee)

    @property
    def is_bankrupt(self):
        """ returns True or False """
        return self.__money <= 0

    def __repr__(self):
        return 'Company (%s)' % self.name


class Person(object):
    """ Represents any person """

    def __init__(self, name, age, sex=None, address=None):
        self.name = name
        self.age = age
        self.sex = sex if sex is not None else '<not specified>'
        self.address = address

    def __repr__(self):
        return '%s, %s years old' % (self.name, self.age)


class Employee(Person):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, age, sex=None, address=None):
        super(Employee, self).__init__(name, age, sex, address)
        self.company = None
        self.__money = 0

    def join_company(self, company):
        # make sure that this person is not employed already
        if not self.is_employed:
            try:
                Company.add_employee(company, self)
                self.company = company
            except ValueError:
                raise
        else:
            raise ValueError(f"Ups, {self.name} is already hired. ({self.company})")

    def become_unemployed(self):
        """ Leave current company """
        if self.is_employed:
            Company.notify_im_leaving(self.company, self)

    def notify_dismissed(self):
        """ Company should call this method when dismissing an employee """
        self.company = None

    def bonus_to_salary(self, company, reward=5):
        """
        Company should call this method on each employee when having a party
        """
        if self in company.employees:
            self.__money += reward
        # make sure person is employed to same company
        # money + 5

    @property
    def is_employed(self):
        """ returns True or False """
        return self.company is not None

    def put_money_into_my_wallet(self, amount):
        """ Adds the indicated amount of money to persons budget """
        self.__money += amount
        # Engineer and Manager will have to use this method to store their
        # salary, because __money is a private attribute

    def show_money(self):
        """ Shows how much money person has earned """
        return print(self.__money)

    @abc.abstractmethod
    def do_work(self):
        """ This method requires re-implementation """
        if self.is_employed:
            pass
        # raise NotImplemented('This method requires re-implementation')

    def __repr__(self):
        if self.is_employed:
            return '%s works at %s' % (self.name, self.company)
        return '%s, unemployed'


class Engineer(Employee):
    def do_work(self):
        """ Engineer work """
        payslip = Company.do_tasks(self.company, self)
        if payslip is not None:
            self.put_money_into_my_wallet(payslip)


class Manager(Employee):
    def do_work(self):
        """ Manager work """
        payslip = Company.write_reports(self.company, self)
        if payslip is not None:
            self.put_money_into_my_wallet(payslip)


def check_yourself():
    """ Now let's operate on objects """

    # create first company
    fruits_company = Company('Fruits', address='Ocean street, 1')
    print(fruits_company)

    # add some employees
    alex = Engineer('Alex', 55)
    alex.join_company(fruits_company)
    alex.do_work()
    alex.show_money()
    fruits_company.show_money()

    # add second company
    doors_company = Company('Windows and doors', address='Mountain ave. 10')
    print(doors_company)

    # Alex wants to work for doors
    alex.join_company(doors_company)
    # ups, already haired
    alex.become_unemployed()
    alex.join_company(doors_company)
    alex.do_work()

    # Bill also wants to work for doors
    bill = Engineer('Bill', 20)
    bill.join_company(doors_company)
    bill.do_work()

    # Jane is a very good manager. She wants to work for fruits
    jane = Manager('Jane', 30)
    jane.join_company(fruits_company)
    # Jane works pretty hard. She writes lots of reports
    jane.do_work()
    jane.do_work()

    # Bill wants Jane to be his manager, he leaves doors and joins fruits
    bill.become_unemployed()
    bill.join_company(fruits_company)

    # doors becomes a bankrupt
    doors_company.go_bankrupt()

    # alex becomes unemployed and goes to fruits
    alex.join_company(fruits_company)

    # fruits company has a celebration party
    fruits_company.make_a_party()

    # results
    fruits_company.show_money()
    doors_company.show_money()
    alex.show_money()
    bill.show_money()
    jane.show_money()
    # print('-' * 10)
    # print("fruits_company:", fruits_company.__dict__)
    # print("doors_company:", doors_company.__dict__)
    # print('-' * 10)
    # print("Alex:", alex.__dict__)
    # print("Bill:", bill.__dict__)
    # print("Jane:", jane.__dict__)


if __name__ == '__main__':
    check_yourself()
