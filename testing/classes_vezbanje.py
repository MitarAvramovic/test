class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_info(self):
        return f"{self.name} ima platu {self._salary}"

    def increase_salary(self, percent):
        self._salary *= (1 + percent / 100)

e1 = Employee(name="Marko", salary=50000)

print(e1.get_info())

e1.increase_salary(20)

print(e1.get_info())

class Manager(Employee):
    def __init__(self, name, salary, departement, bonus):
        super().__init__(name, salary)
        self.departement = departement
        self.bonus  = bonus

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} u {self.departement} i ostvaruje bonus od {self.bonus}"
    
    def total_salary(self):
        return self._salary + self.bonus
    
m1 = Manager("Milos", 100000, "IT", 5000)

print(m1.get_info())

print(m1.total_salary())

m1.increase_salary(50)

print(m1.total_salary())