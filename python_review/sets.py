def list_to_set(nums: List[int]) -> Set[int]:
    ns = set()
    for num in nums:
        ns.add(num)
    return ns

def count_unique_words(words: List[str]) -> int:
    return len(set(words))

def contains_duplicate(words: List[str]) -> bool:
    return len(set(words)) != len(words)
