def check_equal(x: int, y: int) -> bool:
    return x == y

def check_not_equal(x: int, y: int) -> bool:
    return x != y

def check_less_than(x: int, y: int) -> bool:
    return x < y

def check_greater_than(x: int, y: int) -> bool:
    return x > y

def check_less_than_or_equal(x: int, y: int) -> bool:
    return x <= y

def check_greater_than_or_equal(x: int, y: int) -> bool:
    return x >= y

x = 5
y = 6

if x < y:
    print("omg x is less than y")

def pay_bill(balance: int, bill: int) -> int:
    if balance >= bill:
        change = balance - bill
        return change
    return balance

print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))

# if-else test
def get_min(a: int, b: int) -> int:
    if a < b:
        return a
    else:
        return b

def check_range(num: int) -> str:
    if num < 0:
        return "negative"
    elif num == 0:
        return "zero"
    elif num > 0 and num < 10:
        return "positive single digit"
    else:
        return "positive multi digit"

def discount_applies(age: int) -> bool:
    if age < 18 or age >= 65:
        return True
    else:
        return False

def is_truthy(value) -> str:
    if value:
        return "Truthy"
    else:
        return "Falsy"