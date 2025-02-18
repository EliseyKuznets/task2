class Animal:
    def speak(self):
        print("Животное издает звук")

    def eat(self):
        print("Животное ест")


class Dog(Animal):
    def speak(self):
        print("Собака лает: Гав-гав!")

    def fetch(self):
        print("Собака принесла палку")

# Тестовая программа
def test_animal_and_dog():
    animal = Animal()
    print("Демонстрация работы базового класса Animal:")
    animal.speak()
    animal.eat()
    print()

    dog = Dog()
    print("Демонстрация работы производного класса Dog:")
    dog.speak()
    dog.eat()
    dog.fetch()


test_animal_and_dog()