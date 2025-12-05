import pprint
import functools

with open('Day_4/input', 'r') as file:
    lines = file.readlines()

rolls_map = list(map(lambda line: list(map(lambda symbol: 1 if symbol == "@" else 0, line)), lines))


def remove_rolls(rolls_map):
    rolls_map_width = len(rolls_map[0])
    rolls_map_hight = len(rolls_map)
    extended_rolls_map = [[0] * rolls_map_width] + rolls_map + [[0] * rolls_map_width]
    extended_rolls_map = list(map(lambda row: [0] + row + [0], extended_rolls_map))

    removed = 0

    for i in range(0, rolls_map_width):
        for j in range(0, rolls_map_hight):
            if rolls_map[j][i] == 1:
                surrond_rolls = \
                    extended_rolls_map[j][i] + \
                    extended_rolls_map[j + 1][i] + \
                    extended_rolls_map[j + 2][i] + \
                    extended_rolls_map[j][i + 1] + \
                    extended_rolls_map[j + 2][i + 1] + \
                    extended_rolls_map[j][i + 2] + \
                    extended_rolls_map[j + 1][i + 2] + \
                    extended_rolls_map[j + 2][i + 2]
                if surrond_rolls < 4:
                    removed += 1
                    rolls_map[j][i] = 0
    return removed

removed = remove_rolls(rolls_map)
removed_total = removed

print(removed_total)

while removed != 0:
    removed = remove_rolls(rolls_map)
    removed_total += removed

print(removed_total)