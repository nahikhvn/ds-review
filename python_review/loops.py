i = 0
while i < 12:
    print("python")
    i += 1

for i in range(12): # this will iterate and increment without needing to inc in loop body
    print("python")

# notice how you dont have to instantiate a var w/ for loop.

# starting and stopping
for i in range(1, 4): # prints 1, 2, 3 since 1 inclusive and 4 exclusive
    print(i)

# steps param
for i in range(0, 21, 2): # prints increments of 2 from 0 to 20
    print(i)

# revere traversal
for i in range(10, -1, -1): # prints 10 to 0
    print(i)

# or use reversed
for i in reversed(range(0, 11)):
    print(i)

# nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(str(i) + " " + str(j))

# control flow
if True:
    pass # this does nothing

for i in range(0, 7):
    continue # skips all values
    print(i)

for i in range(0, 6):
    break
    print(i)
