# when creating a dictionary, just use curly brackets {}

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    names = []
    for key in age_dict:
        names.append(key) # since the names are the keys
    return names


def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    ages = []
    for key in age_dict:
        age = age_dict[key]
        ages.append(age)
    return ages
def count_characters(word: str) -> Dict[str, int]:
    counts = {}
    for c in word:
        if c not in counts:
            counts[c] = 1 # new char
        else:
            counts[c] += 1
    return counts

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for key in keys:
        if key in my_dict:
            my_dict.pop(key)
    return my_dict
        
def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    return list(age_dict.values())