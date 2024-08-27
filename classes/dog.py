# dog.py

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor containing instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"