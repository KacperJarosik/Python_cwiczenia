# 1. Utworzyć klasę Person, która przy inicjalizacji
# podaje nazwisko (name) i pensje(salary) danej osoby jako dwa osobne atrybuty.
# Zdefiniuj metodę displayCount(),
# która podaje ilu jest pracowników (zmienna personCount).
# Zdefiniuj metodę displayPerson(), która wyświetla imię i nazwisko pracownika.
# Zdefiniuj dwa obiekty danej klasy i wykonaj podane metody.
# Zmień ich parametry.
class Person:
    'klasa podstawowa dla wszystkich osób'
    personCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Person.personCount += 1
        Person.displayCount()

    @staticmethod
    def displayCount():
        print(f'Liczba osób: {Person.personCount}')

    def displayPerson(self):
        print(f'Name : {self.name}, salary: {self.salary}')

    def __del__(self):
        Person.personCount -= 1
        print(f'Skasowano obiekt {self.__class__.__name__}')
        Person.displayCount()


if __name__ == "__main__":
    osoba1 = Person('Anna', 500)
    osoba2 = Person('Piotr', 300)
    osoba1.displayPerson()
    osoba2.displayPerson()
    del osoba1

    input('press any key -- Person')
