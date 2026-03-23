def get_longer_word(word1: str, word2: str) -> str:
    if len(word1) >= len(word2):
        return word1
    else:
        return word2

def print_first_char(word: str) -> None:
    print(word[0])

def print_second_char(word: str) -> None:
    print(word[1])

def print_last_char(word: str) -> None:
    print(word[len(word) - 1])

for c in range(len(word)):
    print(word[c])

for char in word:
    print(char) # doesnt need the indexing notation

# string concatenation
basic = "Hello" + "World"

# string slicing
my_string = "yo whats up"

slice_one = my_string[3, 8] # gives me "what"

def first_n_characters(s: str, n: int) -> str:
    return s[:n]

def last_n_characters(s: str, n: int) -> str: # n is the number of vals we want
    return s[len(s) - n:]

def reverse_string(input_string: str) -> str:
    return input_string[::-1]

def remove_fourth_character(word: str) -> str:
    first_half = word[:3]
    second_half = word[4:]
    return first_half + second_half

# f string formatting
def say_goodbye(name: str, hour: int) -> str:
    return f"Goodbye, {name}. See you again at {hour} o'clock."