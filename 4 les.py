#завдання 1
class Animal:
    def __init__(self,paws,age):
        self.paws = paws
        self.age = age

class Dog(Animal):
    def __init__(self,paws,age):
        super().__init__(paws,age)

class Cat(Animal):
    def __init__(self,paws,age):
        super().__init__(paws,age)

Wolf = Animal(4,3)
Toxa = Dog(4,4)
Murka = Cat(4,2)
print(Toxa.paws,Toxa.age)
print(Murka.paws,Murka.age)