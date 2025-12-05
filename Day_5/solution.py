import pprint
import functools
import itertools

with open('Day_5/input', 'r') as file:
    input = file.read()

ranges, ids = input.split("\n\n")
ranges = list(map(lambda range: list(map(int, range.split('-'))), ranges.split('\n')))
ids = map(int, ids.split("\n"))
fresh = 0

for _id in ids:
    for range_start, range_end in ranges:
        if range_start <= _id <= range_end:
            fresh +=1
            break

print(fresh)


# x.....x
#     x..........x
#                       x....x

ranges.sort(key=lambda x: x[0])
print(ranges)

compressed_ranges = []
previous_start = 0
previous_end = 0

for start, end in ranges:
    if start > previous_end + 1:
        compressed_ranges.append([previous_start, previous_end])
        previous_start = start
        previous_end = end

    previous_end = max(end, previous_end)

compressed_ranges.append([previous_start, previous_end])
print(compressed_ranges)

res2 = functools.reduce(
    lambda x, y: x+ y, 
    map(
        lambda range: range[1]-range[0] +1,
        compressed_ranges[1:]))

print(res2)