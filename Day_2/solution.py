import itertools, functools

with open("Day_2/input", "r") as file:
    input = file.read()

ranges = input.split(",")
res = 0
res2 = 0

def find_factors(n):
    """
    >>> tuple(find_factors(1))
    (1,)
    >>> tuple(find_factors(7))
    (1, 7)
    >>> tuple(find_factors(10))
    (1, 2, 5, 10)
    """
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

def is_silly(s_id):
    """
    >>> is_silly("11")
    True
    >>> is_silly("111")
    True
    >>> is_silly("1212")
    True
    >>> is_silly("123123")
    True
    >>> is_silly("12312312")
    False
    >>> is_silly("34563457")
    False
    >>> is_silly("122112")
    False
    """
    l_id = len(s_id)
    for slice_size in tuple(find_factors(l_id))[:-1]:
        slices = itertools.batched(s_id, n=slice_size)
        if functools.reduce(lambda s1, s2: s1 if s1 == s2 else False, slices):
            return True
        
    return False


for _range in ranges:
    range_start, range_end = _range.split('-')
    for _id in range(int(range_start), int(range_end) + 1):
        s_id = str(_id)
        split = len(s_id) // 2
        if (s_id[:split] == s_id[split:]):
            res += _id
        if (is_silly(s_id)):
            res2 += _id

print(res)
print(res2)