# 2. Utworzyć klasę Employee, która dziedziczy po klasie Person
# i zawiera dodatkowy atrybut Age.
# Zdefiniuj metodę displayEmployee(), która wyświetla nazwę pracownika,
# pensję oraz wiek.

from lab12_01 import Person  # lub skopiować daną klasę z pliku lab12_01.py


class Employee(Person):
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def displayEmployee(self):
        print(f'Name : {self.name}, salary: {self.salary} Age: {self.age}')


if __name__ == "__main__":
    if __name__ == "__main__":
        osoba1 = Employee('Anna', 500, 34)
        osoba2 = Employee('Piotr', 300, 22)
        osoba1.displayEmployee()
        osoba2.displayEmployee()
    input('press any key -- Employee')
