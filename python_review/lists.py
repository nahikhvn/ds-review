my_list = [1, "hello", 3.14, True]

print(my_list[1])
print(my_list[2])
print(my_list[0])
print(len(my_list))

# list operations

my_list = [1, 2, 3]

if len(my_list) > 0:
    print("not empty")

# is equal to:

if my_list:
    print("not empty")


# can check if a value is inside a list too:
if 2 in my_list:
    print("wow")

if 6 not in my_list:
    print("rip")

def count_x(nums: List[int], x: int) -> int:
    count = 0
    for num in nums:
        if num == x:
            count += 1

    return count

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    for n in elements:
        my_list.append(n) # should continue until all elements in second list are iterated
    return my_list


def remove_from_list(my_list: List[int], index: int) -> List[int]:
    my_list.pop(index)
    return my_list


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    for i in range(n):
        my_list.pop()
    return my_list


def find_index(nums: List[int], target: int) -> int:
    return nums.index(target)

def get_last_three_elements(my_list: List[int]) -> List[int]:
    return my_list[-3::]

tup = (1, 2, 3)
print(sum(tup))