import functools

with open("Day_3/input", "r") as file:
    input = file.read()


def max_joltage(bank):
    """
    >>> max_joltage([1, 2, 3])
    23
    >>> max_joltage([3, 2, 1])
    32
    """
    m1 = max(bank[:-1])
    im1 = bank.index(m1)
    m2 = max(bank[im1 + 1 :])
    return m1 * 10 + m2


def max_joltage_2(bank, remaining=12):
    """
    >>> max_joltage_2([1, 2, 3], 2)
    23
    >>> max_joltage_2([3, 2, 1], 2)
    32
    """
    remaining -= 1
    if remaining == 0:
        return max(bank)
    digit = max(bank[:-remaining])
    index = bank.index(digit)
    result = max_joltage_2(bank[index + 1 :], remaining)
    result += digit * (10**remaining)
    return result


banks = list(map(lambda bank: list(map(int, list(bank))), input.split("\n")))
res1 = functools.reduce(lambda x, y: x + y, list(map(max_joltage, banks)))
print(res1)
res2 = functools.reduce(lambda x, y: x + y, list(map(max_joltage_2, banks)))
print(res2)
