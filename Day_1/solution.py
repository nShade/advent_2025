with open('Day_1/input', 'r') as file:
    lines = file.readlines()

def change_position(initial, direction, clicks):
    """
    >>> change_position(1, "R", 1)
    (2, 0)
    >>> change_position(1, "L", 1)
    (0, 1)
    >>> change_position(0, "L", 1)
    (99, 0)
    >>> change_position(1, "L", 2)
    (99, 1)
    >>> change_position(99, "R", 1)
    (0, 1)
    >>> change_position(99, "R", 2)
    (1, 1)
    >>> change_position(7, "L", 300)
    (7, 3)
    >>> change_position(94, "R", 100)
    (94, 1)
    >>> change_position(93, "R", 300)
    (93, 3)
    >>> change_position(0, "R", 1)
    (1, 0)
    """
    if direction == "L": # 0, L, 1
        return (initial - clicks)%100, abs(((100 - initial)%100 + clicks)//100)
    if direction == "R": 
        return (initial + clicks)%100, abs((initial + clicks)//100)

position = 50
zeros_1 = 0
zeros_2 = 0


for line in lines:
    direction, clicks = line[0], int(line[1:])
    position, zr = change_position(position, direction, clicks)
    zeros_1 = zeros_1 + (1 if position == 0 else 0)
    zeros_2 = zeros_2 + zr

print(zeros_1)
print(zeros_2)
