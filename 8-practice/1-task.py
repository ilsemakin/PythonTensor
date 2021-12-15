#!/usr/bin/python3

class Animals:
    def __init__(self, phylum, height, width, weight):
        self.phylum = phylum
        self.height = height
        self.width = width
        self.weight = weight
    
    def info(self):
        print(
            f'My phylum: {self.phylum}\n'
            f'My height: {self.height}\n'
            f'My width: {self.width}\n'
            f'My weight: {self.weight}')
        
class Mammmals(Animals):
    def __init__(self, name_class, phylum, height, width, weight):
        super().__init__(phylum, height, width, weight)
        self.name_class = name_class

    def info(self):
        print(f'My class: {self.name_class}')
        super().info()

class Human(Mammmals):
    def __init__(
            self, name, age, gender, race, eyes, weight,
            name_class, phylum, height, width):
        super().__init__(name_class, phylum, height, width, weight)
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        self.eyes = eyes

    def to_eat(self):
        print("Now I'm full, thanks!")

    def info(self):
        print(
            f'My name: {self.name}\n'
            f'My age: {self.age}\n'
            f'My gender: {self.gender}\n'
            f'My race: {self.race}\n'
            f'My eyes: {self.eyes}')

class Cat(Mammmals):
    def __init__(
            self, name, age, breed, width, weight,
            name_class, phylum, height):
        super().__init__(name_class, phylum, height, width, weight)
        self.name = name
        self.age = age
        self.breed = breed

    def make_sound(self):
        print('Meow')

class Dog(Mammmals):
    def __init__(
            self, name, age, breed, doghouse, weight, 
            name_class, phylum, height, width):
        super().__init__(name_class, phylum, height, width, weight)
        self.name = name
        self.age = age
        self.breed = breed
        self.doghouse = doghouse

    def make_sound(self):
        print('Gav-Gav-Gav')