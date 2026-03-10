message = "this string is stored in a variable"

print(message)
print(message)

capital_of_spain = "madrid"
capital_of_france = "paris"
capital_of_germany = "berlin"

print(capital_of_spain)
print(capital_of_france)
print(capital_of_germany)

# reassigning a variable
message = "message 1"
message = "message 2"

message1, message2 = "hello", "world"
message1, message2 = message2, message1 # swapped values of messages

# variable types
integer = 10
flaot = 10.3
stirng = "hello"
booolean = False
lsit = [1, 2, 3]

stirng = 1 # not recommended, this is dynamic typing

print(type(integer))
print(type(flaot))
print(type(stirng))
print(type(booolean))
print(type(lsit))

print(int(flaot)) # type casting
# cannot type cast incompatible types

null_value = None # this is the no value type, none