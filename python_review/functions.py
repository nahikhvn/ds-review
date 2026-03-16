def greet():
    print("Hello, World!")

def say_goodbye():
    print("Goodbye, World!")

greet() # invocation of the function greet

def print_number(val):
    print(val)

n = 10
print_number(n)

# the function must be defined before its invocation

# functions can have parameters too
def farewell(name):
    msg = "Goodbye, " + name
    print(msg)

farewell("Napoleon")

# multi params
def greet(name, greeting):
    msg = greeting + " " + name
    print(msg)

greet("Socrates", "Yo,")

def two_sum(num, num2):
    total = num + num2
    print(total)

def three_sum(num, num2, num3):
    total = num + num2 + num3
    print(total)

two_sum(6, 7)
three_sum(1, 2, 3)

# intro to returns
def multiply(a, b):
    return a * b

print(multiply(3, 10))

# returns can be of None type too.
# type annotations
def add(x: int, y: int) -> int:
    total = x + y
    return total

x = add(13, 7)
print(x)

# none type return, print returns None
def none_type(name: str) -> None:
    print("Hello, " + name)

# scope testing
n = 10

def add_one(x):
    total = x + 1
    print(total)

add_one(n)
print(n)

n = 100
def print_local_variable(num: int) -> None:
    print(num)

print_local_variable(n)
print(n)

# default parameter values
def greeting(name="World"):
    msg = "Hello, " + name
    print(msg)

def yolo(name, name2, smth="Something"):
    msg = name + " " + name2 + " " + smth
    print(msg)

# parameters may have their own default values, but any param after them must also have default values then