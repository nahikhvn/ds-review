def read_integer() -> int:
    i = int(input())
    return i

def read_float() -> float:
    i = float(input())
    return i

def read_integers() -> List[int]:
    i = input() # cannot cast to int here 1,2,3,4,5
    split = i.split(",")
    nums = []
    for num in split:
        nums.append(int(num))
    return nums

def add_two_numbers() -> int:
    nums = input()
    l = nums.split(",")
    list_to_nums = []
    for num in l:
        list_to_nums.append(int(num))
    return sum(list_to_nums)