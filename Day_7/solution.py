
with open('Day_7/input', 'r') as file:
    input = file.readlines()

rays = list(map(int, list(input[0].replace('S', "1").replace(".", "0"))[:-1]))
splits = 0

for row in input[1:]:
    for i, ray in enumerate(rays):
        if ray != 0 and row[i] == "^":
            rays[i] = 0
            rays[i+1] += ray
            rays[i-1] += ray
            splits += 1

print(splits)
print(sum(rays))
