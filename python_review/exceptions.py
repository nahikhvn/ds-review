def divide_numbers(a: int, b: int) -> None:
    try:
        print(a / b)
    except:
        print("An error occurred!")

def divide_numbers(a: str, b: str) -> None:
    try:
        ca = int(a)
        cb = int(b)
        print(ca / cb)
    except Exception as error:
        print("An error occurred:", error)

# we can can multiple catches, but we use except for catches, more concise -> broad catches
def divide_numbers(a: str, b: str) -> None:
    try:
        ca = int(a)
        cb = int(b)
        print(ca / cb)
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as error:
        print("An error occured:", error)