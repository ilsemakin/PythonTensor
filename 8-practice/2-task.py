#!/usr/bin/python3

class Human:
    def __init__(self, name, age, growth, weight):
        self.name = name
        self.age = age
        self.age = age
        self.growth = growth
        self.weight = weight

class Student(Human):
    def __init__(self, name, age, growth, weight, homeworks):
        super().__init__(name, age, growth, weight)
        self.homeworks = homeworks

    def __eq__(self, other):
        return True if self.homeworks == other.homeworks else False
    
    def __ne__(self, other):
        return True if self.homeworks != other.homeworks else False
    
    def __gt__(self, other):
        return True if self.homeworks > other.homeworks else False

    def __lt__(self, other):
        return True if self.homeworks < other.homeworks else False

    def __ge__(self, other):
        return True if self.homeworks >= other.homeworks else False

    def __le__(self, other):
        return True if self.homeworks <= other.homeworks else False