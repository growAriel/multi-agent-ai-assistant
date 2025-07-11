##List
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])  # Output: apple

fruits.append("blueberry")

print(len(fruits))  # Output: 5

##Tuple
coordinates = (10.0, 20.0)
print(coordinates[0])  # Output: 10.0

##dictionary
person = {"name": "Alice",
           "age": 30,
           "height": 5.5}
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 30
person["is_student"] = False
print(person)  # Output: {'name': 'Alice', 'age': 30, 'height': 5.5, 'is_student': False}

##Set
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}
unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}
print(len(unique_numbers))  # Output: 5

##String
greeting = "Hello, World!"
print(greeting[0])  # Output: H
print(greeting[7:12])  # Output: World
print(greeting.upper())  # Output: HELLO, WORLD!
print(greeting.lower())  # Output: hello, world!
print(greeting.replace("World", "Python"))  # Output: Hello, Python!
print(greeting.split(", "))  # Output: ['Hello', 'World!']
print("Hello" in greeting)  # Output: True
print("Python" not in greeting)  # Output: True

##Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

my_friend = Person("Bob", 25)
print(my_friend.greet())  # Output: Hello, my name is Bob and I am 25 years old.
print(my_friend.name)  # Output: Bob
print(my_friend.age)  # Output: 25  

print(my_friend.__dict__)  # Output: {'name': 'Bob', 'age': 25}
print(type(my_friend))  # Output: <class '__main__.Person'>

##common module
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793
print(math.factorial(5))  # Output: 120
import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10
print(random.choice(fruits))  # Output: Random fruit from the list
import datetime
now = datetime.datetime.now()
print(now)  # Output: Current date and time
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: Formatted current date and time
print(now.year)  # Output: Current year
print(now.month)  # Output: Current month
print(now.day)  # Output: Current day
print(now.hour)  # Output: Current hour
print(now.minute)  # Output: Current minute
print(now.second)  # Output: Current second
print(now.weekday())  # Output: Current day of the week (0=Monday, 6=Sunday)
print(now.isoweekday())  # Output: Current day of the week (1=Monday, 7=Sunday)
print(now.strftime("%A"))  # Output: Current day of the week (e.g., "Monday")
print(now.strftime("%B"))  # Output: Current month (e.g., "January")
print(now.strftime("%Y-%m-%d"))  # Output: Current date (e.g., "2023-10-01")
print(now.strftime("%H:%M:%S"))  # Output: Current time (e.g., "14:30:00")
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: Current date and time (e.g., "2023-10-01 14:30:00")
print(now.strftime("%Y-%m-%d %H:%M:%S %Z"))  # Output: Current date and time with timezone (e.g., "2023-10-01 14:30:00 UTC")
print(now.strftime("%Y-%m-%d %H:%M:%S %z"))  # Output: Current date and time with UTC offset (e.g., "2023-10-01 14: 30:00 +0000")
print(now.strftime("%Y-%m-%d %H:%M:%S %Z %z"))  # Output: Current date and time with timezone and UTC offset (e.g., "2023-10-01 14:30:00 UTC +0000")
print(now.strftime("%Y-%m-%d %H:%M:%S %Z %z %A"))  # Output: Current date and time with timezone, UTC offset, and day of the week (e.g, "2023-10-01 14:30:00 UTC +0000 Sunday")