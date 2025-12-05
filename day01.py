import re
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers
with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

p = 50
part1 = 0
part2 = 0

for line in inp:
    if not line:
        continue

    d = extract_integers(line)[0]

    if d == 0:
        if p == 0:
            part1 += 1
        continue


    if line[0] == "R":
        z = (100 - p) % 100
        if z == 0:
            z = 100

        if z <= d:
            part2 += 1 + (d - z) // 100
        p = (p + d) % 100

    #=="L"
    else:
        z = p % 100
        if z == 0:
            z = 100

        if z <= d:
            part2 += 1 + (d - z) // 100

        p = (p - d) % 100


    if p == 0:
        part1 += 1

print(f"P1: {part1}")
print(f"P2: {part2}")