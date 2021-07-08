from Inheritance.multiple_inheritance.person import Person
from Inheritance.multiple_inheritance.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
