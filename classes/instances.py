# instances.py
from dog import Dog
# Instance attributes are unique to each instance of an object
miles = Dog("Miles", 4)
print(miles)
print(miles.speak("Woof"))

buddy = Dog("Buddy", 9)
print(buddy.speak("Bow wow"))

# Class attributes are the same for all instances
print(miles.species)
print(buddy.species)